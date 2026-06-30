import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file (API keys)
load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Countries to compare (Adzuna country codes)
# fr = France, de = Germany, gb = UK, nl = Netherlands
COUNTRIES = ["fr", "de", "gb", "nl"]

# Job titles to search for
KEYWORDS = ["data analyst", "business analyst", "business intelligence"]

# Number of pages to fetch per search (Adzuna max is 50 results per page)
PAGES = 3

# Empty list that will store every job offer we collect
all_jobs = []

def fetch_jobs(country, keyword, page):
    """
    Calls the Adzuna API for ONE combination of country / keyword / page,
    and returns the list of job offers found.
    """
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": keyword,
        "results_per_page": 50,
        "content-type": "application/json"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error for {country}/{keyword}/page{page}: {response.status_code}")
        return []

    data = response.json()
    return data.get("results", [])

# Triple loop: for each country, for each keyword, for each page
for country in COUNTRIES:
    for keyword in KEYWORDS:
        for page in range(1, PAGES + 1):
            print(f"Extracting: {country} | {keyword} | page {page}")
            results = fetch_jobs(country, keyword, page)

            # Stop fetching further pages if this one returned nothing
            if not results:
                break

            for job in results:
                all_jobs.append({
                    "country": country,
                    "search_keyword": keyword,
                    "title": job.get("title"),
                    "company": job.get("company", {}).get("display_name"),
                    "location": job.get("location", {}).get("display_name"),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "contract_type": job.get("contract_type"),
                    "created": job.get("created"),
                    "description": job.get("description"),
                    "url": job.get("redirect_url"),
                })

            # Pause 1 second between calls to respect API rate limits
            time.sleep(1)

# Convert the list of dictionaries into a structured table (Pandas DataFrame)
df = pd.DataFrame(all_jobs)

print(f"\nTotal job offers extracted: {len(df)}")

# Save the table to a CSV file
df.to_csv("raw_jobs_data.csv", index=False)
print("File saved: raw_jobs_data.csv")