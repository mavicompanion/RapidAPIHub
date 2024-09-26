from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    url = f"https://open-weather13.p.rapidapi.com/city/{city}/EN"
    headers = {
	"x-rapidapi-key": os.getenv("API_KEY"),
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers).json()
    return response

if __name__ == "__main__":
    print('\n***Get Current Weather Conditions***\n')
    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)

