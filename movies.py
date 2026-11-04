from api import get_movies
from helpers import header, create_numerated_list, select_movie, show_movie_info, action_menu
from watchlist import add_to_watchlist, is_movie_in_watchlist
import random

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

def get_random_movie():
    total_pages = get_movies(None, 1 ,"total_pages")
    page = random.randint(1, min(total_pages, 500))

    movielist = get_movies(None, page, "results")
    movie_index = random.randint(0, len(movielist) - 1)

    selected_movie = movielist[movie_index]
    return selected_movie

def show_random_movie(movie):
    header("YOUR RANDOM PICK")
    movie_title = movie.get("title")
    print(movie_title)

def fright_rouelette_menu():
    while True:
        header("FRIGHT ROULETTE")
        print("Can't decide what to watch? \nLet fate decide...")
        print("\nChoose your roulette mode")
        print("1. Completely random")
        # print("2. Random by rating")
        # print("3. Random by release year")
        print("0. Go back")
        choice = input("\nNumber: ")

        if choice == "1":
            movie = get_random_movie()
            show_random_movie(movie)
            fright_roulette_sub_menu()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
            continue

def fright_roulette_sub_menu():
    print("\nWhat would you like to do?")
    print("1. Spin again")
    print("2. View movie details")
    print("3. Add to watchlist")
    print("4. Back to roulette")
    print("0. Main Menu")
    choice = input("\nNumber: ")

    match choice:
        case "1":
            pass
        # Spin again
        case "2":
            pass
        # View movie details
        case "3":
            pass
        # Add to watchlist
        case "4":
            pass
        # Back to roulette
        case "0":
            pass
        # Main Menu
        case _:
            print("Invalid choice. Please try again.")