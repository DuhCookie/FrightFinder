from helpers import header, console, create_table, get_menu_input, show_movie_info, action_menu
from logger import logger
from movies import show_random_movie, get_random_movie
from watchlist import add_to_watchlist


def fright_roulette_menu():
    """
    Displays the Fright Roulette menu and handles the user's choice.

    Users can choose between different roulette modes to get a
    random horror movie recommendation or go back to the main menu.
    """
    while True:
        header("FRIGHT ROULETTE")
        console.print("\nCan't decide what to watch? \nLet fate decide...", style="italic")
        menu_options = [
            "Completely random",
            "Spin by rating",
            "Spin by release year",
            "Go back"
        ]
        menu = create_table("Choose your roulette mode!", menu_options)
        console.print(menu)
        choice = get_menu_input(len(menu_options))

        if choice == 1 or choice == 2 or choice == 3:
            action = play_roulette_round(choice)
            if action == "main menu":
                break
            else:
                continue
        else:
            break

def roulette_movie_menu(movie):
    """
    Displays the roulette movie menu and handles the user's choice.

    User can spin again, view more details about the movie,
    add the movie to their watchlist, return to the roulette menu,
    or go back to the main menu.

    :param movie: A dictionary containing information about the selected movie.
    :return: 'again', 'back', or 'main menu', depending on the user's choice.
    """
    while True:
        menu_options = [
            "Spin again",
            "View movie details",
            "Add to watchlist",
            "Back to roulette",
            "Main Menu"
        ]
        show_random_movie(movie)

        menu = create_table("What do you want to do?", menu_options)
        console.print(menu)
        choice = get_menu_input(len(menu_options))

        match choice:
            case 1:
                return "again"
            case 2:
                show_movie_info(movie)
                action = action_menu(movie.get("title"), watchlist=False)
                if action == "add":
                    add_to_watchlist(movie.get("title"), movie)
            case 3:
                add_to_watchlist(movie.get("title"), movie)
            case 4:
                return "back"
            case 5:
                return "main menu"

def roulette_rating_menu():
    """
    Displays the roulette rating menu and handles the user's choice.

    Users can choose from a set of predefined minimum ratings,
    enter a custom rating, return to the roulette menu,
    or go back to the main menu.

    The selected rating is used to filter the movies
    that can be chosen by the roulette.

    :return: A minimum rating, 'back', or 'main menu',
    depending on the user's choice.
    """
    while True:
        header("FRIGHT ROULETTE: SPIN BY RATING")

        menu_options = [
            "5.0+",
            "6.0+",
            "7.0+",
            "8.0+",
            "Custom rating",
            "Go back",
            "Main Menu"
        ]

        menu = create_table("What is your minimum rating?", menu_options)
        console.print(menu)
        choice = get_menu_input(len(menu_options))

        match choice:
            case 1:
                return 5
            case 2:
                return 6
            case 3:
                return 7
            case 4:
                return 8
            case 5:
                while True:
                    try:
                        min_rating = float(console.input("Enter a custom rating: "))
                        logger.info(f"User entered custom rating: '{min_rating}'.")
                        if 1 <= min_rating <= 10:
                            return min_rating
                        else:
                            console.print("\nPlease pick a number between 1 and 10.\n")
                            logger.warning("Invalid rating entered. Input is out of range.")
                    except ValueError:
                        console.print("\nPlease enter a valid number.\n")
                        logger.warning("Invalid rating entered. Input is not a number")
                        continue
            case 6:
                return "back"
            case 7:
                return "main menu"

def roulette_year_menu():
    """
    Displays the roulette year menu and handles the user's choice.

    Users can choose a horror movie era to filter the random
    movie selection by release date, return to
    the previous menu or go back to the main menu.

    :return: A tuple with the selected release dates,
    'back', or 'main menu', depending on the user's choice.
    """
    while True:
        header("FRIGHT ROULETTE: SPIN BY YEAR")
        menu_options = [
            "Classic Horror (before 1980)",
            "80s Horror",
            "90s Horror",
            "2000s Horror",
            "Modern Horror (2010+)",
            "Go back",
            "Main Menu"
        ]

        menu = create_table("Choose your era!", menu_options)
        console.print(menu)
        choice = get_menu_input(len(menu_options))

        match choice:
            case 1:
                return None, "1979-12-31"
            case 2:
                return "1980-01-01", "1989-12-31"
            case 3:
                return "1990-01-01", "1999-12-31"
            case 4:
                return "2000-01-01", "2009-12-31"
            case 5:
                return "2010-01-01", None
            case 6:
                return "back"
            case 7:
                return "main menu"

def play_roulette_round(roulette_mode):
    """
    Handles one round of Fright Roulette.

    Depending on the selected roulette mode, a random horror movie
    is chosen either completely at random, by rating, or by release
    year. After viewing the result, the user can spin again, return
    to the previous menu, or go back to the main menu.

    :param roulette_mode: The selected roulette mode.
    1 = completely random, 2 = spin by rating, 3 = spin by release year.
    :return: The action 'back' or 'main menu', depending on the user's choice.
    """
    while True:
        if roulette_mode == 2:
            logger.info("User selected: Spin by rating.")
            rating = roulette_rating_menu()
            if rating == "main menu":
                return "main menu"
            elif rating == "back":
                return "back"

            movie = get_random_movie(rating)

        elif roulette_mode == 3:
            logger.info("\nUser selected: Spin by year.")
            result = roulette_year_menu()
            if result == "main menu":
                return "main menu"
            elif result == "back":
                return "back"
            else:
                min_release_date, max_release_date = result

            movie = get_random_movie(None, min_release_date, max_release_date)
        else:
            logger.info("User selected: Completely random.")
            movie = get_random_movie()

        action = roulette_movie_menu(movie)
        if action == "again":
            continue
        elif action == "back":
            return "back"
        elif action == "main menu":
            return "main menu"
