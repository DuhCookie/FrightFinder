from helpers import header
from keywords import search_keyword
from movies import discover_movies, fright_rouelette_menu
from watchlist import watchlist_menu

from rich.console import Console
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

def show_main_menu():
    header("FRIGHTFINDER")
    console.print("\nFind the perfect horror movie for your movie night.\n", style="italic")
    console.print("What do you want to do?")
    console.print("1. Discover Horror Movies")
    console.print("2. Fright roulette")
    console.print("3. My watchlist")
    console.print("4. Exit")

def main():
    while True:
        show_main_menu()
        choice = input("\nNumber: ")

        match choice:
            case "1":
                while True:
                    keyword_id, keyword = search_keyword()
                    action = discover_movies(keyword_id, keyword)

                    if action == "main menu":
                        break
                    elif action == "search again":
                        continue
            case "2":
                fright_rouelette_menu()
            case "3":
                watchlist_menu()
            case "4":
                exit()
            case _:
                console.print("Invalid Choice. Please try again.")
                continue

main()
