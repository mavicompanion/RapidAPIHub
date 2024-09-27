from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_earnings():
    url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/modules"
    querystring = {"ticker":"AAPL","module":"earnings"}
    headers = {
	"x-rapidapi-key": os.getenv("API_KEY_FINANCE"),
	"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    return response



x = get_earnings()
pprint(x['body']['earnings']['maxAge'])