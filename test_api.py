import os
import requests
from dotenv import load_dotenv

# Charge les variables du fichier .env dans l'environnement Python
load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Construction de l'URL selon la doc Adzuna (pays = fr, page = 1)
url = "https://api.adzuna.com/v1/api/jobs/fr/search/1"

# Paramètres de la requête
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "what": "data analyst",
    "results_per_page": 20,
    "content-type": "application/json"
}

# Envoi de la requête GET à l'API
response = requests.get(url, params=params)

# Affiche le code de statut HTTP (200 = succès)
print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Nombre total de résultats:", data.get("count"))
    print("Premier résultat:", data["results"][0])
else:
    print("Erreur:", response.text)