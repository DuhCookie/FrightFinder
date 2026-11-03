from api import get_movies
from helpers import header, create_numerated_list, select_movie, show_movie_info, action_menu
from watchlist import add_to_watchlist

def show_movielist(movielist, keyword):
    if not movielist:
        print(f"\nNo horror movies were found for the keyword '{keyword}'. Please try a different keyword.")
        return None
    else:
        header("FOUND MOVIES")
        create_numerated_list(movielist, "release_date")
        #TODO: DRY WITH NUMERATED LIST FUNCTION
        for index, result in enumerate(movielist, start= 1):
            release_date = result.get("release_date")

            if release_date:
                release_year = release_date.split("-")[0]
            else:
                release_year = "TBA"

            print(f"{index}. {result.get('title')} ({release_year})")
        return "Found"

def discover_movie(keyword_id, keyword):

    movielist = get_movies(keyword_id)

    while True:
        result = show_movielist(movielist, keyword)
        if result is None:
            return "search again"

        selected_movie, movie_index = select_movie(movielist)
        if selected_movie is None:
           return "main menu"

        movie_title = show_movie_info(selected_movie)
        action = action_menu(movie_title, selected_movie)
        if action == "add":
            add_to_watchlist(movie_title, selected_movie)
        elif action == "back":
            continue
        else:
            return "main menu"
