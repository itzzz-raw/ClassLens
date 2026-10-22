# CLASSLENS

**ClassLens: Class Record Management System with Program Outcome Validation using eXtreme Gradient Boosting (XGBoost)**

ClassLens is a class record management system for the College of Computer Studies at Camarines Sur Polytechnic Colleges (CSPC). It supports class record processing, Course Outcome (CO) to Program Outcome (PO) validation, and early academic risk prediction. The project is designed for BSCS, BSIT, and BSIS curricula for 2019, 2022, and 2023.

> This repository contains the project source code. Do not upload identifiable student records or other restricted data. Use only data approved for sharing, and anonymize it before committing.

## Project goals

- Organize and process class records in `.xlsx` and `.csv` formats.
- Map assessment tasks to Course Outcomes and Course Outcomes to Program Outcomes.
- Calculate outcome attainment and support curriculum compliance reporting.
- Use XGBoost to estimate early academic risk from available academic assessment data.

## Main features

- Import and process class record files.
- Anonymize student identifiers for analysis.
- Maintain curriculum and CO-to-PO mappings.
- Calculate PO attainment and classify outcomes as Met, Partially Met, or Not Met, using configured thresholds.
- Display early-risk predictions in an instructor dashboard.

## Methodology

The system workflow is:

1. The instructor provides a supported class record file and selects the applicable class and curriculum.
2. The system validates and processes assessment scores and applies its student-identifier anonymization process.
3. Assessment tasks are associated with Course Outcomes, and Course Outcomes are associated with Program Outcomes using the configured mappings.
4. The system calculates outcome attainment from the mapped assessment data and reports the results using the configured thresholds.
5. The early-risk component uses an XGBoost model to generate risk predictions from available academic assessment data. Its predictions are presented separately from the PO-attainment calculations.

The model should be trained and evaluated using authorized, appropriately prepared data. Record the dataset scope, feature preparation, target labels, train/test method, and evaluation metrics here after confirming them against the implemented code and approved research methodology.

## Evaluation and results

Add the measured results here after completing system and model evaluation. Do not report estimates as observed results.

| Evaluation item | Result |
|---|---|
| Dataset used and number of records | To be completed from the approved dataset |
| Model evaluation method | To be completed from the actual experiment |
| Model metrics (for example, precision, recall, F1-score, and confusion matrix) | To be completed from actual evaluation |
| Functional testing summary | To be completed from recorded test results |
| External IT expert evaluation | To be completed if conducted |

## Technology stack

- **Frontend:** React, React Router, Tailwind CSS, Axios, Vite
- **Backend:** Python, FastAPI, Uvicorn, Pydantic
- **Data and machine learning:** Pandas, NumPy, XGBoost, scikit-learn for evaluation
- **Database:** PostgreSQL with SQLAlchemy and psycopg
- **Spreadsheet support:** openpyxl

Confirm this list against the current source code and dependency files before submission.

## Repository structure

```text
ClassLens/
├── backend/       # FastAPI application and data/model processing
├── frontend/      # React and Vite user interface
├── README.md
└── requirements.txt
```

The exact files may change as development continues.

## Local setup

### Prerequisites

- Python 3.11 or a compatible version used by the backend
- Node.js 18 or newer
- PostgreSQL

### Backend

```bash
cd backend
python -m venv .venv
```

Activate the environment, then install the backend dependencies. If the dependency file is in the repository root, use:

```bash
pip install -r ../requirements.txt
```

Start the API using the entry point defined by the backend source. For example, if the application object is `app` in `main.py`:

```bash
uvicorn main:app --reload
```

### Frontend

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Use the local address printed by Vite. Follow any additional environment-variable or database setup instructions in the source code.

## Privacy and data handling

This project may process academic records. Keep raw records, names, student numbers, credentials, API keys, and other restricted information out of public commits. Share datasets only when the data owner has explicitly allowed public release. Use a sanitized sample dataset for demonstrations when needed.

## Development team

- Rovilyn A. Agnote
- Mary Joyce N. Moico
- Rhea Lizza B. Sanglay

## License

No license is currently specified. Add a license only after the team decides how the source code may be reused.
