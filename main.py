from helpers import header
from keywords import search_keyword
from movies import discover_movie, fright_rouelette_menu
from watchlist import watchlist_menu

def show_main_menu():
    header("FRIGHTFINDER")
    print("🩸🪦🧟🎃🐈‍⬛🕯️🔪🩸")
    print("Find the perfect horror movie for your movie night.\n")
    print("What do you want to do?")
    print("1. Discover Horror Movies")
    print("2. Fright roulette")
    print("3. My watchlist")
    print("4. Exit")

def main():
    while True:
        show_main_menu()
        choice = input("\nNumber: ")

        match choice:
            case "1":
                while True:
                    keyword_id, keyword = search_keyword()
                    action = discover_movie(keyword_id, keyword)

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
                print("Invalid Choice. Please try again.")
                continue

main()
