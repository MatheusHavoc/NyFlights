# NYC Flights - Flight Delay Analysis

This repository contains an exploratory notebook about New York flight delays and a new lightweight Python profiling layer under `src/nyflights/`.

## What this PR changes

The notebook is still the source of the full analysis. The Python code added in this PR does not claim to reproduce every chart or business question from the notebook. It provides a safer project structure around the original work:

- local CSV/Excel ingestion with explicit errors;
- normalized column names;
- missing-value and numeric profiling outputs;
- duplicate-row metrics;
- an optional `delay_summary_by_destination.csv` when the dataset includes `dest` and `dep_delay`;
- tests for the reusable ingestion and profiling functions.

## Repository structure

```text
.
├── NYF.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── images/
├── notebooks/
├── src/nyflights/
├── tests/
├── requirements.txt
└── README.md
```

## Dataset requirement

The pipeline expects a local file such as `data/raw/nyflights.csv`. That file is not committed to this repository. Without the dataset, you can inspect the code and run unit tests, but you cannot execute the project pipeline end to end.

## How to run when the dataset is available

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m nyflights.pipeline --input data/raw/nyflights.csv --output data/processed
```

On Linux/macOS, replace the activation command with `source .venv/bin/activate`.

## Outputs

Always generated when the input file exists:

- `data/processed/missing_summary.csv`
- `data/processed/numeric_summary.csv`
- `data/processed/dataset_metrics.json`

Generated only when the expected flight-delay columns exist:

- `data/processed/delay_summary_by_destination.csv`

## Current limitations

- The original notebook still contains the richer exploratory analysis.
- Dataset source and schema are not yet fully documented.
- Delay business rules beyond the 120-minute threshold should be extracted from the notebook in future work.
- This PR intentionally does not invent a production pipeline or claim model execution.
