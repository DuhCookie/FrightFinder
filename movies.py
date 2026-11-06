from api import get_movies
from helpers import header, select_movie, show_movie_info, action_menu, create_table
from watchlist import add_to_watchlist, is_movie_in_watchlist
import random

from rich.console import Console
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

def show_movielist(movielist, keyword):
    if not movielist:
        console.print(f"\nNo horror movies were found for the keyword '{keyword}'. Please try a different keyword.")
        return None
    else:
        header("FOUND MOVIES")
        movie_table = create_table(None, movielist, False, "title", True)
        console.print(movie_table)
        return "Found"

def discover_movies(keyword_id, keyword):
    movielist = get_movies(keyword_id)

    while True:
        result = show_movielist(movielist, keyword)
        if result is None:
            return "search again"

        # handle_movie_selection(movielist) for discover movies and watchlist

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
    console.print("\nFate has decided...", style="italic")
    movie_title = movie.get("title")
    console.print(f"\nYour movie is [bold #ED2D2D]{movie_title}[/]", style="italic")

def fright_rouelette_menu():
    while True:
        header("FRIGHT ROULETTE")
        console.print("\nCan't decide what to watch? \nLet fate decide...", style="italic")
        menu_text = [
            "Completely random",
            "Spin by rating",
            "Spin by release year",
            "Go back"
        ]
        menu = create_table("Choose your roulette mode!", menu_text)
        console.print(menu)
        choice = console.input("[bold on #800000]Number:[/] ")

        if choice == "1" or choice == "2" or choice == "3":
            action = play_roulette_round(choice)
            if action == "main menu":
                break
            else:
                continue
        elif choice == "4":
            break
        else:
            console.print("Invalid option. Please try again.")
            continue

def roulette_movie_menu(movie):
    while True:
        menu_text = [
            "Spin again",
            "View movie details",
            "Add to watchlist",
            "Back to roulette",
            "Main Menu"
        ]
        show_random_movie(movie)

        menu = create_table("What do you want to do?", menu_text)
        console.print(menu)
        choice = console.input("[bold on #800000]Number:[/] ")

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
            case "5":
                return "main menu"
            case _:
                console.print("Invalid choice. Please try again.")
                continue

def roulette_rating_menu():
    while True:
        header("FRIGHT ROULETTE: SPIN BY RATING")

        menu_text = [
            "5.0+",
            "6.0+",
            "7.0+",
            "8.0+",
            "Custom rating",
            "Go back",
            "Main Menu"
        ]

        menu = create_table("What is your minimum rating?", menu_text)
        console.print(menu)
        choice = console.input("[bold on #800000]Number:[/] ")

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
                        min_rating = float(console.input("Enter a custom rating: "))
                        if 1 <= min_rating <= 10:
                            return min_rating
                        else:
                            console.print("\nPlease pick a number between 1 and 10.\n")
                    except ValueError:
                        console.print("\nPlease enter a valid number.\n") #TODO: logging
                        continue
            case "6":
                return "back"
            case "7":
                return "main menu"
            case _:
                console.print("Invalid Choice. Please try again.")
                continue

def roulette_year_menu():
    while True:
        header("FRIGHT ROULETTE: SPIN BY YEAR")
        menu_text = [
            "Classic Horror (before 1980)",
            "80s Horror",
            "90s Horror",
            "2000s Horror",
            "Modern Horror (2010+)",
            "Go back",
            "Main Menu"
        ]

        menu = create_table("Choose your era!", menu_text)
        console.print(menu)
        choice = console.console.input("[bold on #800000] Number[/]: ")

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
                return "back"
            case "7":
                return "main menu"
            case _:
                console.print("Invalid Choice. Please try again.")
                continue

def play_roulette_round(roulette_mode):
    while True:
        if roulette_mode == "2":
            rating = roulette_rating_menu()
            if rating == "main menu":
                return "main menu"
            elif rating == "back":
                return "back"

            movie = get_random_movie(rating)

        elif roulette_mode == "3":
            result = roulette_year_menu()
            if result == "main menu":
                return "main menu"
            elif result == "back":
                return "back"
            else:
                min_release_date, max_release_date = result

            movie = get_random_movie(None, min_release_date, max_release_date)
        else:
            movie = get_random_movie()

        action = roulette_movie_menu(movie)
        if action == "again":
            continue
        elif action == "back":
            return "back"
        elif action == "main menu":
            return "main menu"



