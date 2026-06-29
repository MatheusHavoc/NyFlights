from __future__ import annotations

import argparse
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

import pandas as pd

LOGGER = logging.getLogger(__name__)


class DataValidationError(ValueError):
    """Raised when the input dataset does not match the expected contract."""


@dataclass(frozen=True)
class ProjectConfig:
    """Configuration for a portfolio data pipeline."""

    project_name: str
    default_dataset: str
    required_columns: tuple[str, ...] = ()
    date_columns: tuple[str, ...] = ()


CONFIG = ProjectConfig(
    project_name="NYC Flights delay analysis",
    default_dataset="nyflights.csv",
)


def normalize_column_name(column: object) -> str:
    """Return a stable snake_case-like column name for downstream analysis."""
    return str(column).strip().lower().replace(" ", "_").replace("-", "_")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of `df` with normalized column names."""
    cleaned = df.copy()
    cleaned.columns = [normalize_column_name(column) for column in cleaned.columns]
    return cleaned


def load_dataset(path: str | Path, required_columns: Sequence[str] = ()) -> pd.DataFrame:
    """Load a CSV or Excel dataset and validate required columns when provided."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    LOGGER.info("Loading dataset from %s", dataset_path)
    suffix = dataset_path.suffix.lower()
    if suffix == ".csv":
        df = pd.read_csv(dataset_path)
    elif suffix in {".xlsx", ".xls"}:
        df = pd.read_excel(dataset_path)
    else:
        raise DataValidationError(f"Unsupported file format: {suffix}")

    df = normalize_columns(df)
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    return df


def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Build a column-level null-count and null-percentage summary."""
    total_rows = len(df)
    summary = pd.DataFrame({"column": df.columns, "missing_count": df.isna().sum().values})
    summary["missing_pct"] = 0.0 if total_rows == 0 else summary["missing_count"] / total_rows
    return summary.sort_values(["missing_count", "column"], ascending=[False, True]).reset_index(drop=True)


def duplicate_summary(df: pd.DataFrame) -> dict[str, int]:
    """Return row-count and duplicate-count metrics."""
    return {"row_count": int(len(df)), "duplicate_rows": int(df.duplicated().sum())}


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        return pd.DataFrame()
    return numeric_df.describe().transpose().reset_index(names="column")


def run_pipeline(input_path: str | Path, output_dir: str | Path = "data/processed") -> dict[str, Any]:
    """Run the reusable data-quality pipeline and write analysis artifacts."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = load_dataset(input_path, required_columns=CONFIG.required_columns)
    missing = missing_summary(df)
    numeric = numeric_summary(df)
    duplicates = duplicate_summary(df)

    missing.to_csv(output_path / "missing_summary.csv", index=False)
    numeric.to_csv(output_path / "numeric_summary.csv", index=False)
    (output_path / "dataset_metrics.json").write_text(json.dumps(duplicates, indent=2), encoding="utf-8")

    LOGGER.info("Pipeline completed for %s", CONFIG.project_name)
    return {"rows": duplicates["row_count"], "duplicate_rows": duplicates["duplicate_rows"], "outputs": str(output_path)}


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(description=CONFIG.project_name)
    parser.add_argument("--input", required=True, help="Path to the raw CSV or Excel file.")
    parser.add_argument("--output", default="data/processed", help="Directory for generated artifacts.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
    args = build_parser().parse_args(argv)
    try:
        result = run_pipeline(args.input, args.output)
    except Exception:
        LOGGER.exception("Pipeline failed")
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
