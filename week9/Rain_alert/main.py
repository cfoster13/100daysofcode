import requests
import os
from dotenv import load_dotenv

load_dotenv()

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("WEATHER_API_KEY") # Get your API key from the .env file, Sign up on openweathermap to get your own API key

parameters = {
    "lat": 51.5074,
    "lon": -0.1278,
    "appid": api_key,
    "cnt": 4}

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()


weather_id = weather_data["list"][0]["weather"][0]["id"]
weather_description = weather_data["list"][0]["weather"][0]["description"]

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
        

if will_rain:
    print("Bring an umbrella")
else:
    print(f"No rain today, it's {weather_description}")

