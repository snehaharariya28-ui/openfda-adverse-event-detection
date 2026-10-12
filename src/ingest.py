import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENFDA_API_KEY")
BASE_URL = "https://api.fda.gov/drug/event.json"

DRUGS = [
    "metformin", "atorvastatin", "lisinopril", "amlodipine", "omeprazole",
    "sertraline", "ibuprofen", "levothyroxine", "albuterol", "metoprolol",
    "gabapentin", "hydrochlorothiazide", "losartan", "citalopram", "prednisone"
]

RECORDS_PER_DRUG = 1000  # max allowed per single request

for drug in DRUGS:
    params = {
        "search": f'patient.drug.medicinalproduct:"{drug}"',
        "limit": RECORDS_PER_DRUG,
        "api_key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        file_path = f"data/raw/{drug}.json"
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"{drug}: saved {len(data['results'])} records to {file_path}")
    else:
        print(f"{drug}: FAILED, status code {response.status_code}")