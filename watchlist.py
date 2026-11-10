import json
from helpers import header, show_movie_info, action_menu, create_table, select_from_list, console
from logger import logger


def watchlist_menu():
    """
    Displays the watchlist menu and handles the user's choice.

    Users can select a movie from their watchlist, view its details,
    remove it from the watchlist or go back to the main menu.
    """

    while True:
        header("MY WATCHLIST")
        watchlist = view_watchlist()

        result = select_from_list(watchlist)
        if result is None:
            break
        else:
            selected_movie, movie_index = result

        movie_title = show_movie_info(selected_movie)
        action = action_menu(movie_title, watchlist=True)

        if action == "remove":
            remove_from_watchlist(selected_movie, movie_index)
        elif action == "back":
            continue

def add_to_watchlist(movie_title, movie):
    """
    Adds a movie to the watchlist if it is not already added.
    :param movie_title: The title of the selected movie.
    :param movie: A dictionary containing information about the selected movie.
    """
    if not is_movie_in_watchlist(movie):
        watchlist = open_watchlist("r")
        watchlist.append(movie)
        with open("watchlist.json", "w") as file:
            json.dump(watchlist, file, indent= 4)

        print(f"\n{movie_title} has been added to your watchlist!")
        logger.info(f"Added {movie_title} to watchlist.")
    else:
        print(f"\n{movie_title} has already been added to your watchlist!")
        logger.warning(f"{movie_title} is already in watchlist.")

def view_watchlist():
    """
    Displays the user's watchlist in a table.
    :return:A list of dictionaries containing the movies in the watchlist.
    """
    watchlist = open_watchlist("r")

    if not watchlist:
        print("You haven't added any movies to your watchlist yet.")
    else:
        watchlist_table = create_table(None, watchlist, False, "title")
        console.print(watchlist_table)
    return watchlist

def remove_from_watchlist(selected_movie, index):
    """
    Removes a movie from the watchlist.
    :param selected_movie:  A dictionary containing information about the selected movie.
    :param index: The index of the selected movie in the watchlist.
    """
    while True:
        print(f"\nAre you sure you want to remove '{selected_movie.get("title")}' from your watchlist?")
        choice = console.input("[bold on #800000]Y/N:[/] ").capitalize()

        if choice == "Y":
            watchlist = open_watchlist("r")
            watchlist.pop(index)

            with open("watchlist.json", "w") as file:
                json.dump(watchlist, file, indent=4)

            print(f"\n{selected_movie.get("title")} has been removed from your watchlist!")
            logger.info(f"Removed {selected_movie.get("title")} from watchlist.")
            break
        elif choice == "N":
            break
        else:
            print("\nInvalid choice. Please try again")
            continue

def is_movie_in_watchlist(movie):
    """
    Checks if a movie is already in the watchlist.
    :param movie: A dictionary containing information about the movie.
    :return: True if the movie is already in the watchlist, otherwise False.
    """
    movie_id = movie.get("id")
    watchlist = open_watchlist("r")
    id_list = [movie.get("id") for movie in watchlist]

    if movie_id in id_list:
        return True
    else:
        return False

def open_watchlist(mode= "r"):
    """
    Opens and loads the watchlist.
    :param mode: The file mode used to open the watchlist file.
    :return: A list of dictionaries containing the movies in the watchlist.
    """
    with open("watchlist.json", mode) as file:
        watchlist = json.load(file)
    return watchlist
