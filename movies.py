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
            add_to_watchlist(movie_title, selected_movie)
        elif action == "back":
            continue

def get_random_movie(vote_average=None, min_release_date=None, max_release_date=None):
    total_pages = get_movies(None, 1 ,"total_pages", vote_average, min_release_date, max_release_date)
    page = random.randint(1, min(total_pages, 500))

    movielist = get_movies(None, page, "results", vote_average, min_release_date, max_release_date)
    movie_index = random.randint(0, len(movielist) - 1)

    selected_movie = movielist[movie_index]
    return selected_movie

def show_random_movie(movie):
    header("YOU'VE SPUN THE FRIGHT ROULETTE!")
    print("Fate has decided...")
    movie_title = movie.get("title")
    print(f"\nYour movie is: {movie_title}")

def fright_rouelette_menu():
    while True:
        header("FRIGHT ROULETTE")
        print("Can't decide what to watch? \nLet fate decide...")
        print("\nChoose your roulette mode!")
        print("1. Completely random")
        print("2. Spin by rating")
        print("3. Spin by release year")
        print("0. Go back")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                while True:
                    movie = get_random_movie()
                    action = fright_roulette_sub_menu(movie)
                    if action == "again":
                        continue
                    elif action == "back":
                        break
                    elif action == "main menu":
                        return
            case "2":
                rating = random_rating_menu()
                if not rating:
                    return

                while True:
                    movie = get_random_movie(rating)
                    action = fright_roulette_sub_menu(movie)
                    if action == "again":
                        continue
                    elif action == "back":
                        break
                    elif action == "main menu":
                        return
            case "3":
                result = random_year_menu()
                if result == "main menu":
                    return
                else:
                    min_release_date, max_release_date = result

                while True:
                    movie = get_random_movie(None, min_release_date, max_release_date)
                    action = fright_roulette_sub_menu(movie)
                    if action == "again":
                        continue
                    elif action == "back":
                        break
                    elif action == "main menu":
                        return
            case "0":
                break
            case _:
                print("Invalid option. Please try again.")
                continue

def fright_roulette_sub_menu(movie):
    while True:
        show_random_movie(movie)
        print("\nWhat would you like to do?")
        print("1. Spin again")
        print("2. View movie details")
        print("3. Add to watchlist")
        print("4. Back to roulette")
        print("0. Main Menu")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                return "again"
            case "2":
                show_movie_info(movie)
                action = action_menu(movie.get("title"), watchlist=False)
                if action == "add":
                    add_to_watchlist(movie.get("title"), movie)
            case "3":
                add_to_watchlist(movie.get("title"), movie)
            case "4":
                return "back"
            case "0":
                return "main menu"
            case _:
                print("Invalid choice. Please try again.")
                continue

def random_rating_menu():
    while True:
        header("FRIGHT ROULETTE: SPIN BY RATING")
        print("What is your minimum rating?")
        print("\n1. 5.0+")
        print("2. 6.0+")
        print("3. 7.0+")
        print("4. 8.0+")
        print("5. Custom rating")
        print("0. Main Menu")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                return 5
            case "2":
                return 6
            case "3":
                return 7
            case "4":
                return 8
            case "5":
                while True:
                    try:
                        min_rating = float(input("Enter a custom rating: "))
                        if 1 <= min_rating <= 10:
                            return min_rating
                        else:
                            print("\nPlease pick a number between 1 and 10.\n")
                    except ValueError:
                        print("\nPlease enter a valid number.\n") #TODO: logging
                        continue
            case "0":
                return None
            case _:
                print("Invalid Choice. Please try again.")
                continue

def random_year_menu():
    while True:
        header("FRIGHT ROULETTE: SPIN BY YEAR")
        print("Choose your era!")
        print("\n1. Classic Horror (before 1980)")
        print("2. 80s Horror")
        print("3. 90s Horror")
        print("4. 2000s Horror")
        print("5. Modern Horror (2010+)")
        print("6. Main Menu")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                return None, "1979-12-31"
            case "2":
                return "1980-01-01", "1989-12-31"
            case "3":
                return "1990-01-01", "1999-12-31"
            case "4":
                return "2000-01-01", "2009-12-31"
            case "5":
                return "2010-01-01", None
            case "6":
                return "main menu"
            case _:
                print("Invalid Choice. Please try again.")
                continue



