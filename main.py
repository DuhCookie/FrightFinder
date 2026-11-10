from helpers import header, create_table, get_menu_input, console
from keywords import search_keyword
from movies import discover_movies
from roulette import fright_roulette_menu
from watchlist import watchlist_menu
from logger import logger


def show_main_menu():
    """
    Displays the title of the application and the different options the user
    can choose from.

    :return: A list of available menu options.
    """

    header("FRIGHTFINDER")
    console.print("\nFind the perfect horror movie for your movie night.", style="italic")
    menu_options = [
        "Discover Horror Movies",
        "Fright roulette",
        "My watchlist",
        "Exit"
    ]
    menu = create_table("What do you want to do?", menu_options)
    console.print(menu)
    return menu_options

def main():
    """
    Runs the main application loop.
    """
    while True:
        menu_options = show_main_menu()
        choice = get_menu_input(len(menu_options))

        match choice:
            case 1:
                logger.info("User selected: Discover Horror Movies.")
                while True:
                    keyword_id, keyword = search_keyword()
                    action = discover_movies(keyword_id, keyword)

                    if action == "main menu":
                        break
                    elif action == "search again":
                        continue
            case 2:
                logger.info("User selected: Fright Roulette.")
                fright_roulette_menu()
            case 3:
                logger.info("User selected: My watchlist.")
                watchlist_menu()
            case 4:
                logger.info("Application closed.")
                exit()

logger.info("Application started.")
main()
