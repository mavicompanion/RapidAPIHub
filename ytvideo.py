from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import re

load_dotenv()


def get_video_id_regex(video_url):
  match = re.search(r'v=([A-Za-z0-9_-]{11})', video_url)
  if match:
    return match.group(1)
  else:
    return None



def get_video(video_url):
    url = "https://yt-api.p.rapidapi.com/dl"
    querystring = {"id":"6r2Kbaai22s"}

    video_id = get_video_id_regex(video_url)
    querystring["id"] = video_id

    headers = {
        "x-rapidapi-key": os.getenv("API_KEY_YT"),
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    return response
    

if __name__ == "__main__":
    video_url = str(input("Enter video URL: "))
    m = get_video(video_url)
    x = m["adaptiveFormats"]
    pprint(x)
    # webbrowser.open(x)
