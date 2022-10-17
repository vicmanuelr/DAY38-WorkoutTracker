import requests
import os
import datetime as dt

NUTRI_APP_ID = os.environ.get("APP_ID")
NUTRI_API_KEY = os.environ.get("API_KEY")
NUTRI_HEADERS = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_QUERY = {
 "query": input("Tell me which exercises you did: "),
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 173,
 "age": 35
}
response = requests.post(url=NUTRI_ENDPOINT, headers=NUTRI_HEADERS, json=NUTRI_QUERY)
response.raise_for_status()
data = response.json()
print(data)
