from helpers import header, create_table, get_menu_input
from keywords import search_keyword
from movies import discover_movies, fright_rouelette_menu
from watchlist import watchlist_menu
from logger import logger

from rich.console import Console
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

def show_main_menu():
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
    logger.info("Application started.")
    while True:
        menu_options = show_main_menu()
        choice = get_menu_input(len(menu_options))

        match choice:
            case 1:
                logger.info("User selected: Discover Horror Movies")
                while True:
                    keyword_id, keyword = search_keyword()
                    action = discover_movies(keyword_id, keyword)

                    if action == "main menu":
                        break
                    elif action == "search again":
                        continue
            case 2:
                logger.info("User selected: Fright Roulette")
                fright_rouelette_menu()
            case 3:
                logger.info("User selected: My watchlist")
                watchlist_menu()
            case 4:
                logger.info("Application closed")
                exit()

main()
