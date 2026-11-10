from logger import logger
from dotenv import load_dotenv
import os
import requests

load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
TOKEN = os.getenv("TOKEN")


def get_keywords(given_keyword):
    """
    Gets keywords from the TMDB API that match the given keyword.
    :param given_keyword: The keyword entered by the user.
    :return: A list of dictionaries containing information about the retrieved keywords.
    """
    params = {
        "query": given_keyword,
        "page": 1
    }

    return get_api_data("https://api.themoviedb.org/3/search/keyword", params, key="results")

def get_movies(keyword_id=None, page=1, key="results", vote_average=None, min_release_date=None, max_release_date=None):
    """
    Gets horror movies from the TMDB API.

    The function can return movies based on a keyword, minimum
    rating, release dates or a combination of these filters.

    :param keyword_id: The ID of the keyword used to filter movies.
    :param page: The page number of the results to retrieve.
    :param key: The key of the value that should be returned.
    :param vote_average: The minimum movie rating.
    :param min_release_date: The minimum release date.
    :param max_release_date: The maximum release date.
    :return: A list of dictionaries containing information about the retrieved movies.
    """
    params = {
        "page": page,
        "with_genres": 27,
        "with_keywords": keyword_id,
        "vote_average.gte": vote_average,
        "primary_release_date.gte": min_release_date,
        "primary_release_date.lte": max_release_date

    }

    return get_api_data("https://api.themoviedb.org/3/discover/movie", params, key)

def get_api_data(url, params, key):
    """
    Retrieves data from the TMDB API.

    A request is sent to the API using the provided URL and parameters.

    :param url: The URL of the API endpoint.
    :param params: The parameters used in the request.
    :param key: The key of the value that should be returned.
    :return: The requested data or None if the request fails.
    """
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        logger.info("API request succesful.")
        return data.get(key)

    else:
        print(f"It seems that something went wrong. Status code: {response.status_code}")
        logger.error(f"API request failed. TMDB returned status code: {response.status_code}.")
        return None

