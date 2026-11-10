from api import get_movies
from helpers import header, show_movie_info, action_menu, create_table, select_from_list, console
from watchlist import add_to_watchlist
from logger import logger
import random


def show_movielist(movielist, keyword):
    """
    Displays the list of movies found for the selected keyword.
    If no movies are found, a message is shown to the user.

    :param movielist: The list of movies found for the keyword.
    :param keyword: The keyword used to search for movies.
    :return: 'Found' if movies were found, otherwise None.
    """

    if not movielist:
        console.print(f"\nNo horror movies were found for the keyword '{keyword}'. Please try a different keyword.")
        logger.warning(f"No horror movies found for keyword: '{keyword}'.")
        return None
    else:
        header("FOUND MOVIES")
        movie_table = create_table(None, movielist, False, "title", True)
        console.print(movie_table)
        return "Found"

def discover_movies(keyword_id, keyword):
    """
    Handles the entire process of discovering movies based on a given keyword.

    Users can view a list of movies, select a movie to see more
    information, add movies to their watchlist and search for another
    keyword.

    :param keyword_id: The ID of the selected keyword.
    :param keyword: The keyword used to find movies.
    :return: The action 'search again' or 'main menu', depending on the user's choice.
    """
    movielist = get_movies(keyword_id)

    while True:
        result = show_movielist(movielist, keyword)
        if result is None:
            return "search again"

        result = select_from_list(movielist)
        if result is None:
           return "main menu"
        else:
            selected_movie, movie_index = result

        movie_title = show_movie_info(selected_movie)
        action = action_menu(movie_title)
        if action == "add":
            add_to_watchlist(movie_title, selected_movie)
        elif action == "back":
            continue

def get_random_movie(vote_average=None, min_release_date=None, max_release_date=None):
    """
    Gets a random movie from the API.

    A random page of movie results is selected first, after which
    a random movie from that page is chosen. The search can be
    filtered by rating and release date.

    :param vote_average: Minimum rating of the movie.
    :param min_release_date: Earliest release date. Format = "year-month-day".
    :param max_release_date: Latest release date. Format = "year-month-day".
    :return: The dictionary of a randomly selected movie.
    """
    total_pages = get_movies(None, 1 ,"total_pages", vote_average, min_release_date, max_release_date)
    page = random.randint(1, min(total_pages, 500))

    movielist = get_movies(None, page, "results", vote_average, min_release_date, max_release_date)
    movie_index = random.randint(0, len(movielist) - 1)

    selected_movie = movielist[movie_index]
    logger.info(f"Randomly selected: '{selected_movie.get("title")}'")
    return selected_movie

def show_random_movie(movie):
    """
    Displays the movie selected by the Fright Roulette.

    :param movie: The movie's dictionary.
    """
    header("YOU'VE SPUN THE FRIGHT ROULETTE!")
    console.print("\nFate has decided...", style="italic")
    movie_title = movie.get("title")
    console.print(f"\nYour movie is [bold #ED2D2D]{movie_title}[/]", style="italic")



