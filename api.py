# HTTP requests naar TMDB

from dotenv import load_dotenv
import os
import requests

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

url_movie = "https://api.themoviedb.org/3/discover/movie"

def get_keywords(given_keyword):
    url = f"https://api.themoviedb.org/3/search/keyword"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "query": given_keyword,
        "page": 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        keywords = response.json()
        return keywords.get("results")

    else:
        print(f"It seems that something went wrong. Status code: {response.status_code}")
        return None