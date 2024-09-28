from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import json
import matplotlib.pyplot as plt


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


if __name__ == "__main__":
    x = get_earnings()

    stockname = x["meta"]["symbol"]
    earningsdaterevenue = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["raw"]
    earningsdate = x["body"]["earnings"]["earningsChart"]["earningsDate"][0]["fmt"]

    print(f"The estimated revenue for {stockname} by {earningsdate} is: {earningsdaterevenue}")

