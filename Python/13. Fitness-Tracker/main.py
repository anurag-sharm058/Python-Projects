import requests
import os
from datetime import datetime
today_date = datetime.now().strftime("%d/%m/%Y")
current_time =  datetime.now().strftime("%X")

WEIGHT_KG = 62
GENDER = "male"
HEIGHT_CM = 180
AGE = 20

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("API_ID")
post_spreadsheet_endpoint = "https://api.sheety.co/0d663047b20857a566bb50551646ae4d/copyOfMyWorkouts/workouts"
TOKEN = os.environ.get("SHEET_TOKEN")

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}


response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
result = response.json()
calories =  result["exercises"][0]["nf_calories"]
duration = result["exercises"][0]["duration_min"]
exercise = result["exercises"][0]["name"].title()

sheety_parameters = {
    "workout":{
        "Date": today_date,
        "Time": current_time,
        "Exercise":exercise,
        "Duration":duration,
        "Calories":calories,
    }
}
bearer_auth = {
    "Authorization": f"Bearer {TOKEN}"
}
sheety_response = requests.post(url=post_spreadsheet_endpoint, json=sheety_parameters, headers=bearer_auth)
sheety_response.raise_for_status()
print(sheety_response)
