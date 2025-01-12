import requests
from datetime import datetime
import smtplib
import time

my_email = "xerneas01best@gmail.com"
gmail_pass = "fyanbhodjvgweohg"

MY_LAT = 51.46725595826274
MY_LONG = -0.21261439754229183

def is_iss_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_lat = float(iss_response.json()["iss_position"]["latitude"])
    iss_lng = float(iss_response.json()["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_lng <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT, # Location for Putney Bridge
        "lng": MY_LONG,
        "time_format": 24,
    }
    response = requests.get("https://api.sunrisesunset.io/json/", params=parameters)
    response.raise_for_status()
    sunrise = int(response.json()["results"]["sunrise"].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, gmail_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look Up \n\nThe ISS is above you in the sky."
        )