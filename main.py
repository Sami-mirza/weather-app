import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()
    if response.status_code == 200:
        city_name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print(f"\nWeather in {city_name}")
        print(f"Temperature : {temp}°C")
        print(f"Condition   : {description}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")
    else:
        if response.status_code == 404:
            print("City not found. Please check the spelling and try again.")
        else:
            print(f"Something went wrong. Error: {data['message']}")
city = input("Enter city name: ")
get_weather(city)   
