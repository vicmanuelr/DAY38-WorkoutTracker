import requests
import os
from datetime import datetime, date, time


# -------------------------------------- NUTRITIONIX API ------------------------------------------------ #

def get_exercise() -> list:
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
    exercises_list = data['exercises']
    return exercises_list


# -------------------------------------------- SH+EETY API --------------------------------------------#
def new_entry(exercises: list):
    auth_header = os.environ.get("AUTH_HEADER")
    headers = {
        "Authorization": auth_header
    }
    sheet_endpoint = os.environ.get("SHEETY_ENDPOINT")
    for exercise in exercises:
        entry = {
            "workout": {
                "date": date.today().strftime("%d/%m/%Y"),
                "time": datetime.now().time().isoformat(timespec='seconds'),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(headers=headers, url=sheet_endpoint, json=entry)
        print(response.text)


new_entry(get_exercise())
