# ConnectToCare

ConnectToCare is a portfolio project for analyzing healthcare appointment attendance and presenting no-show risk in a clinic-coordinator dashboard.

This project is designed to demonstrate Informatics skills across the full workflow:

`data cleaning -> database design -> predictive modeling -> user-facing application -> usability testing`

## Planned features

- Clean and document a public or synthetic appointment dataset
- Store structured data in SQLite
- Explore factors associated with missed appointments
- Compare interpretable classification models
- Display appointment trends and risk levels in Streamlit
- Test the dashboard with simulated clinic-coordinator users
- Document limitations, fairness concerns, and ethical boundaries

## Project structure

```text
connecttocare/
├── app/                 # Streamlit application
├── data/raw/            # Original data; do not commit sensitive data
├── data/processed/      # Cleaned, generated data
├── notebooks/           # Exploratory and modeling notebooks
├── src/                 # Reusable Python modules
├── tests/               # Automated tests
├── requirements.txt
├── CLAUDE.md
└── README.md
```

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate       # Windows PowerShell
pip install -r requirements.txt
streamlit run app/main.py
```

## Safety and scope

Use only public, anonymized, or synthetic data. This is an educational decision-support project and must not be used for clinical decisions.
