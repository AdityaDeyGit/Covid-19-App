import requests
import os
from datetime import datetime
from twilio.rest import Client

MY_COUNTRY = "India"
API_ENDPOINT = "https://api.covid19api.com/summary"
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
TODAY = datetime.now()
TODAY_DATE = TODAY.strftime("%d/%m/%Y")
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
client = Client(ACCOUNT_SID, AUTH_TOKEN)

response = requests.get(API_ENDPOINT)
response.raise_for_status()
data = response.json()
countries = data["Countries"]
country_data = list(filter(lambda country: country["Country"] == MY_COUNTRY, countries))[0]

date_text = f"For Date: {TODAY_DATE}\n"
new_confirmed = f"New Confirmed: {country_data['NewConfirmed']}\n"
new_deaths = f"New Deaths: {country_data['NewDeaths']}\n"
new_recovered = f"New Recovered: {country_data['NewRecovered']}\n"
total_confirmed = f"Total Confirmed: {country_data['TotalConfirmed']}\n"
total_deaths = f"Total Deaths: {country_data['TotalDeaths']}\n"
total_recovered = f"Total Recovered: {country_data['TotalRecovered']}\n"

message = client.messages \
                .create(
                     body=f"{date_text}{new_confirmed}{new_deaths}{new_recovered}{new_recovered}{total_confirmed}"
                          f"{total_deaths}{total_recovered}",
                     from_='+13202335691',
                     to=PHONE_NUMBER,
                 )
print(message.sid)














