import random
import textwrap

from rich.console import Console
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

def header(title):
    icon = get_icon()
    border = "꒷꒦︶꒷꒦︶꒷꒦" * 4
    title = f"{icon} {title} {icon}"
    console.print()
    console.print(border, style="#CF0000")
    console.print(title.center(len(border)), style="bold #ED2D2D")
    console.print(border, style="#CF0000")

def create_numerated_list(received_list, key, with_releaseyear=False):
    if with_releaseyear:
        for index, result in enumerate(received_list, start=1):
            release_date = result.get("release_date")

            if release_date:
                release_year = release_date.split("-")[0]
            else:
                release_year = "TBA"

            console.print(f"{index}. {result.get(key)} ({release_year})")
    else:
        for index, result in enumerate(received_list, start=1):
            console.print(f"{index}. {result.get(key).capitalize()}")

def action_menu(movie_title, watchlist=False):
    if watchlist:
        action = f"Remove {movie_title} from watchlist"
    else:
        action = f"Add {movie_title} to watchlist"

    while True:
        console.print("\nWhat would you like to do?")
        console.print(f"1. {action}")
        console.print("2. Go back")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                if watchlist:
                    return "remove"
                else:
                    return "add"
            case "2":
                return "back"
            case _:
                console.print("Invalid choice. Please try again")
                continue

def select_movie(movielist):
    while True:
        console.print("\nChoose a movie by entering its number. \nEnter 0 to return to the main menu.")
        choice = int(input("Number: "))

        if 1 <= choice <= len(movielist):
            selected_movie = movielist[choice - 1]
            console.print(f"Chosen movie: {selected_movie.get("title")}")
            return selected_movie, choice - 1
        elif choice == 0:
            return None, None
        else:
            console.print("\nYour selection is not on the list. Please try again.")
            continue

def show_movie_info(movie):
    title = movie.get("title")
    rating = movie.get("vote_average")
    release_date = movie.get("release_date")

    if rating == 0:
        rating = "Not yet rated"
    else:
        rating = f"{rating:.1f}"

    if not release_date:
        release_date = "TBA"

    header("MOVIE INFO")
    console.print(f"\nTitle: {title}\n")
    console.print(f"Summary: {textwrap.fill(movie.get("overview"), width= 70)}\n")
    console.print(f"Rating: {rating}")
    console.print(f"Release date: {release_date}")
    console.print(f"Language: {movie.get("original_language")}")

    return title

def get_icon():
    icons = {
        1: "🕯️",
        2: "🎃",
        3: "🩸",
        4: "🔪",
        5: "🕸️",
        6: "🐈‍⬛",
        7: "𐕣",
        8: "💉",
        9: "💀",
        10: "🫀",
        11: "ִִֶֶָ🥀",
        12: "🕷"
    }
    icon_number = random.randint(1, len(icons))
    return icons.get(icon_number)

# def handle_movie_selection(movielist):
#     selected_movie, movie_index = select_movie(movielist)
#     if selected_movie is None:
#         return "main menu"
#
#     movie_title = show_movie_info(selected_movie)
#     action = action_menu(movie_title, selected_movie)
#     if action == "add":
#         return "add"
#     elif action == "remove":
#         return "remove"
#     elif action == "back":
#         return "back"
#     else:
#         return "main menu"