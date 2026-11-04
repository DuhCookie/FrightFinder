import json
from helpers import create_numerated_list, header, select_movie, show_movie_info, action_menu

def watchlist_menu():
    while True:
        header("MY WATCHLIST")
        watchlist = view_watchlist()

        selected_movie, movie_index = select_movie(watchlist)
        if selected_movie is None:
            break

        movie_title = show_movie_info(selected_movie)
        action = action_menu(movie_title, watchlist=True)

        if action == "remove":
            remove_from_watchlist(selected_movie, movie_index)
        elif action == "back":
            continue
        else:
            return "main menu"

def add_to_watchlist(movie_title, movie):
    watchlist = open_watchlist("r")
    watchlist.append(movie)

    with open("watchlist.json", "w") as file:
        json.dump(watchlist, file, indent= 4)

    print(f"{movie_title} has been added to your watchlist!")

def view_watchlist():
    watchlist = open_watchlist("r")

    if not watchlist:
        print("You haven't added any movies to your watchlist yet.")
    else:
        create_numerated_list(watchlist, "title")
    return watchlist

def remove_from_watchlist(selected_movie, index):
    while True:
        print(f"Are you sure you want to delete '{selected_movie.get("title")}' from your watchlist?")
        choice = input("Y/N: ").capitalize()

        if choice == "Y":
            watchlist = open_watchlist("r")
            watchlist.pop(index)

            with open("watchlist.json", "w") as file:
                json.dump(watchlist, file, indent=4)

            print(f"{selected_movie.get("title")} has been removed from your watchlist!")
            break
        elif choice == "N":
            break
        else:
            print("Invalid choice. Please try again")
            continue

def is_movie_in_watchlist(movie):
    movie_id = movie.get("id")
    watchlist = open_watchlist("r")
    id_list = [movie.get("id") for movie in watchlist]

    if movie_id in id_list:
        return None
    else:
        return "not in list"

def open_watchlist(mode= "r"):
    with open("watchlist.json", mode) as file:
        watchlist = json.load(file)
    return watchlist
