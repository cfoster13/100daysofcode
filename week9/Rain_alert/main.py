import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("WEATHER_API_KEY") # Get your API key from the .env file, Sign up on openweathermap to get your own API
account_sid = os.getenv("TWILIO_SID") # Get your Account SID from the .env file
auth_token = os.getenv("TWILIO_AUTH_TOKEN") # Get your Auth Token from the
my_mobile_number = os.getenv("MY_MOBILE_NUMBER") # Get your mobile number from the .env file
twilio_virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER") # Get your Twilio number from the .env file

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_=f"whatsapp:{twilio_virtual_number}",
        to=f"whatsapp:{my_mobile_number}"
    )

    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"No rain today, it's {weather_description}",
        from_=f"whatsapp:{twilio_virtual_number}",
        to=f"whatsapp:{my_mobile_number}"
    )

