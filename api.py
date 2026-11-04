import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

def get_keywords(given_keyword):
    params = {
        "query": given_keyword,
        "page": 1
    }

    return get_api_data("https://api.themoviedb.org/3/search/keyword", params, key="results")

def get_movies(keyword_id=None, page=1, key="results"):
    # release_date = f"{release_year}-01-01"
    params = {
        "page": page,
        "with_genres": 27,
        "with_keywords": keyword_id,
        # TODO: "vote_average.gte": vote_average,
        # "primary_release_year": release_year
        # "primary_release_date.gte": release_date
    }

    return get_api_data("https://api.themoviedb.org/3/discover/movie", params, key)

def get_api_data(url, params, key):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get(key)

    else:
        print(f"It seems that something went wrong. Status code: {response.status_code}")
        return None

