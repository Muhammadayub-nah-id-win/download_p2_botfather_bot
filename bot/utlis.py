import requests
from os import load_dotenv, getenv
import json

load_dotenv()

RAPID_KEY = getenv('RAPID_KEY')

def download_instagram():
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": "https://www.instagram.com/reel/DHn2qIuM6V2/?igsh=MTRqZmZ0bjllZ3ozNA=="}

    headers = {
        "X-RapidAPI-Key": RAPID_KEY,
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    result = json.loads(response.text)
    print(result)

download_instagram()




