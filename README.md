# NYC Flights - Flight Delay Analysis

Professionalized data project for analyzing flight delays in New York airport data. The original notebook remains available, and reusable Python code now lives under `src/`.

## Staff Data Engineer assessment

This is a useful junior portfolio project because it starts from concrete operational questions and turns raw flight records into delay indicators. The main gap was project engineering: the logic lived only in a notebook and there was no reproducible package, test surface or dependency file.

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
│   ├── __init__.py
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
└── README.md
```

## What changed

- Added a Python package with typed, logged and documented pipeline functions.
- Added data-quality outputs for missing values, numeric summaries and duplicates.
- Added tests for ingestion, column normalization and artifact generation.
- Added conventional `data`, `images`, `notebooks` and `tests` folders.
- Added `.gitignore`, `requirements.txt` and MIT `LICENSE`.

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
python -m nyflights.pipeline --input data/raw/nyflights.csv --output data/processed
```

On Linux/macOS, replace the activation command with `source .venv/bin/activate`.

## Dataset

The expected input file is `data/raw/nyflights.csv`. The dataset is not committed to the repository, so place it locally before running the pipeline.

## Original analysis

The original notebook answers questions about long delays, descriptive statistics, destination behavior and derived flight metrics. The new Python pipeline does not remove that work; it extracts reusable project infrastructure around the analysis.

## Current limitations

- The notebook still contains the richest exploratory analysis.
- Dataset source and schema should be documented in more detail.
- Business rules for delay thresholds should be moved from notebook cells into tested Python functions.
- A SQL version of the main aggregations would strengthen the Engineering signal.
