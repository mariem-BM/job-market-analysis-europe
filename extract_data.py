import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Liste des pays qu'on veut comparer (codes Adzuna)
# fr = France, de = Allemagne, gb = UK, nl = Pays-Bas
COUNTRIES = ["fr", "de", "gb", "nl"]

# Liste des métiers qu'on cherche
KEYWORDS = ["data analyst", "business analyst", "business intelligence"]

# Nombre de pages à récupérer par recherche (50 résultats/page max chez Adzuna)
PAGES = 3

# Liste vide qui va accumuler toutes les offres trouvées
all_jobs = []

def fetch_jobs(country, keyword, page):
    """
    Fonction qui appelle l'API Adzuna pour UNE combinaison
    pays / mot-clé / page, et retourne la liste des offres trouvées.
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
        print(f"Erreur pour {country}/{keyword}/page{page}: {response.status_code}")
        return []

    data = response.json()
    return data.get("results", [])

# Triple boucle : pour chaque pays, pour chaque mot-clé, pour chaque page
for country in COUNTRIES:
    for keyword in KEYWORDS:
        for page in range(1, PAGES + 1):
            print(f"Extraction: {country} | {keyword} | page {page}")
            results = fetch_jobs(country, keyword, page)

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

            time.sleep(1)

df = pd.DataFrame(all_jobs)
print(f"\nTotal d'offres extraites: {len(df)}")

df.to_csv("raw_jobs_data.csv", index=False)
print("Fichier sauvegardé: raw_jobs_data.csv")