# Data & BI Job Market Analysis – Europe

## Overview
This project analyzes the job market for Data Analyst, Business Analyst, and Business Intelligence roles across four European countries (France, Germany,UK, Netherlands), using real job postings collected through the Adzuna API.

## Objectives

- Measures job posting volume by country and role category
- Identify the most frequently requested technical skills per country
- Compare average minimum salaries across countries

## Tec Stack

- **Python** (requests, pandas)- data extraction and cleaning
- **Adzuna API** - job posting data source
- **Power BI** - interactive dashboard
- **Git/GitHub** - Version control

## Project Structure
ob-market-analysis-europe/
│
├── extract_data.py        # Queries the Adzuna API and saves raw job data
├── clean_data.py           # Cleans data, removes duplicates, detects skills
├── analyze_data.py         # Statistical summary (countries, skills,salaries)
├── raw_jobs_data.csv       # Raw extracted dataset
├── clean_jobs_data.csv     # Cleaned, analysis-ready dataset
└── README.md

## Methodology

1- **Extraction** : Queried the Adzuna API across 4 countries × 3 job-title keywords × 3 pages (50 results/page), collecting approximately 1,800 job 
   postings.

2- **Cleaning** : removed duplicate postings (the same job can appear under multiple keyword searches), parsed publication dates, and standardized text fields.

3- **Skill detection** : Applied regex pattern matching with word boundaries (`\b`) to reliably detect skill mentions (Python, SQL, Power BI, Excel, 
   etc.) within job descriptions, avoiding false positives from substring 
   matches (e.g. "R" inside "manager"). 

4- **Analysis** : aggregated results by country and keyword to compare 
   demand, skill requirements, and salary data.

## Key Findings

- Germany shows the highest average minimum salary among the four countries 
  analyzed.
- Power BI and SQL are the most frequently requested tools across all 
  countries.
- [Additional findings will be added following the Power BI dashboard build]

## How to Run

```bash
git clone https://github.com/YOUR-USERNAME/job-market-analysis-europe.git
cd job-market-analysis-europe


python3 -m venv venv
source venv/bin/activate

pip install requests python-dotenv pandas
```

Create a `.env` file with your own Adzuna API credentials: ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key

Run the pipeline:
```bash
python3 extract_data.py
python3 clean_data.py
python3 analyze_data.py
```

## Next Steps

- Build a full interactive Power BI dashboard
- Add time-based trend analysis on posting activity
- Extend coverage to additional countries

## Author

Maryem Ben Massaoud
