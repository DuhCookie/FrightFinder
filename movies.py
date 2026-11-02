from api import get_movies
from helpers import header
import textwrap

def show_movielist(movielist):
    if not movielist:
        print("\nThere are no available keywords found based on your entry. Please try again.")
        return None
    else:
        header("FOUND MOVIES")

        for index, result in enumerate(movielist, start= 1):
            release_date = result.get("release_date")

            if release_date:
                release_year = release_date.split("-")[0]
            else:
                release_year = "TBA"

            print(f"{index}. {result.get('title')} ({release_year})")
        return "Found"

def select_movie(movielist):
    while True:
        print("\nChoose a movie by entering its number. \nEnter 0 to return to the main menu.")
        choice = int(input("Number: "))

        if 1 <= choice <= len(movielist):
            selected_movie = movielist[choice - 1]
            print(f"Chosen movie: {selected_movie.get("title")}")
            return selected_movie
        elif choice == 0:
            return None
        else:
            print("\nYour selection is not on the list. Please try again.")
            continue

def show_movie_info(movie):
    title = movie.get("title")
    rating = movie.get("vote_average")
    release_date = movie.get("release_date")

    if rating == 0:
        rating = "Not yet rated"

    if not release_date:
        release_date = "TBA"

    header("MOVIE INFO")
    print(f"Title: {title}\n")
    print(f"Summary: {textwrap.fill(movie.get("overview"), width= 70)}\n")
    print(f"Rating: {rating:.1f}")
    print(f"Release date: {release_date}")

    movie_menu(title)

def movie_menu(movie_title):
    print("\nWhat would you like to do?")
    print(f"1. Add {movie_title} to watchlist")
    print("2. Go back")
    print("3. Return to main menu")
    choice = input("\nNumber: ")

def save_movie():
    pass

def discover_movie(keyword_id, keyword):
    while True:
        movielist = get_movies(keyword_id)

        result = show_movielist(movielist)
        if result is None:
            return None

        selected_movie = select_movie(movielist)
        if selected_movie is None:
            return None

        show_movie_info(selected_movie)
