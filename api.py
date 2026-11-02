import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")

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

    return get_api_results(url, headers, params)

def get_movies(keyword_id):
    # release_date = f"{release_year}-01-01"
    url = "https://api.themoviedb.org/3/discover/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "page": 1,
        "with_genres": 27,
        "with_keywords": keyword_id,
        # "vote_average.gte": vote_average,
        # "primary_release_year": release_year
        # "primary_release_date.gte": release_date
    }

    return get_api_results(url, headers, params)

def get_api_results(url, headers, params):
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("results")

    else:
        print(f"It seems that something went wrong. Status code: {response.status_code}")
        return None