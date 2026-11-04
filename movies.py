from api import get_movies
from helpers import header, create_numerated_list, select_movie, show_movie_info, action_menu
from watchlist import add_to_watchlist, is_movie_in_watchlist

def show_movielist(movielist, keyword):
    if not movielist:
        print(f"\nNo horror movies were found for the keyword '{keyword}'. Please try a different keyword.")
        return None
    else:
        header("FOUND MOVIES")
        create_numerated_list(movielist, "title", with_releaseyear=True)
        return "Found"

def discover_movie(keyword_id, keyword):

    movielist = get_movies(keyword_id)

    while True:
        result = show_movielist(movielist, keyword)
        if result is None:
            return "search again"

        # handle_movie_selection(movielist)

        selected_movie, movie_index = select_movie(movielist)
        if selected_movie is None:
           return "main menu"

        movie_title = show_movie_info(selected_movie)
        action = action_menu(movie_title)
        if action == "add":
            if is_movie_in_watchlist(selected_movie):
                add_to_watchlist(movie_title, selected_movie)
            else:
                print(f"{movie_title} is already added to your watchlist!")

        elif action == "back":
            continue
        else:
            return "main menu"
