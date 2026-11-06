import random
import textwrap

from rich.console import Console
from rich.table import Table
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

from logger import logger

def create_table(title, rows, menu=True, key=None, with_releaseyear=False):
    if not title:
        table = Table(show_header=False, border_style="#CF0000")
    else:
        table = Table(title=title, title_style="bold on #800000", show_header=False, border_style="#CF0000")

    numbered_rows = create_numerated_list(rows, menu, key, with_releaseyear)
    table.add_column(style="bold #ED2D2D")

    for number, text in numbered_rows:
        table.add_row(number, text)

    print()
    return table

def header(title):
    icon = get_random_icon()
    border = "꒷꒦︶꒷꒦︶꒷꒦" * 4
    title = f"{icon} {title} {icon}"
    console.print()
    console.print(border, style="#CF0000")
    console.print(title.center(len(border)), style="bold #ED2D2D")
    console.print(border, style="#CF0000")

def create_numerated_list(received_list, menu=False, key=None, with_releaseyear=False):
    numerated_list = []
    if with_releaseyear:
        for index, result in enumerate(received_list, start=1):
            release_date = result.get("release_date")

            if release_date:
                release_year = release_date.split("-")[0]
            else:
                release_year = "TBA"
            movie_text = (f"{index}", f"{result.get(key).capitalize()} [italic #878686]({release_year})[/]")
            numerated_list.append(movie_text)
    elif menu:
        for index, text in enumerate(received_list, start=1):
            menu_text = (f"{index}", text)
            numerated_list.append(menu_text)
    else:
        for index, result in enumerate(received_list, start=1):
            movie_text = (f"{index}", result.get(key).capitalize())
            numerated_list.append(movie_text)

    return numerated_list

def action_menu(movie_title, watchlist=False):
    if watchlist:
        action = f"Remove {movie_title} from watchlist"
    else:
        action = f"Add {movie_title} to watchlist"

    while True:
        menu_options = [
            action,
            "Go back"
        ]
        menu = create_table("What do you want to do?", menu_options)
        console.print(menu)
        choice = get_menu_input(len(menu_options))

        if choice == 1:
            if watchlist:
                return "remove"
            else:
                return "add"
        else:
            return "back"

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
    console.print(f"\n[bold]Title:[/] {title}\n")
    console.print(f"[bold]Summary:[/] {textwrap.fill(movie.get("overview"), width= 70)}\n")
    console.print(f"[bold]Rating:[/] {rating}")
    console.print(f"[bold]Release date:[/] {release_date}")
    console.print(f"[bold]Language:[/] {movie.get("original_language")}")

    return title

def get_random_icon():
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

def get_menu_input(option_count):
    while True:
        try:
            choice = int(console.input("[bold on #800000]Number:[/] "))
            if 1 <= choice <= option_count:
                logger.info(f"User selected menu option {choice}.")
                return choice
            else:
                console.print(f"\nInvalid choice. \nPlease pick a number between 1 and {option_count}.\n")
                logger.warning("Invalid menu option. Input is out of range.")
                continue
        except ValueError:
            console.print("\nPlease enter a valid number.\n")
            logger.warning("Invalid menu option. Input is not an integer.")
            continue

def select_from_list(current_list, list_type="movies"):
    if list_type == "movies":
        subject = "movie"
        prompt = "Choose a movie by entering its number. \nEnter 0 to return to the main menu.\n"
        key = "title"
    else:
        subject = "keyword"
        prompt = "Choose a keyword by entering its number. \nEnter 0 to search for another keyword.\n"
        key = "name"

    while True:
        try:
            console.print(prompt)
            choice = int(console.input("[bold on #800000]Number:[/] "))

            if 1 <= choice <= len(current_list):
                selected = current_list[choice - 1]
                selected_subject = selected.get(key).capitalize()
                console.print(f"\n[bold on #800000]Chosen {subject}:[/] {selected_subject}")
                logger.info(f"User selected {subject} '{selected.get(key)}'.")

                if list_type == "movies":
                    return selected, choice - 1
                else:
                    selected_id = selected.get("id")
                    return selected_id, selected_subject

            elif choice == 0:
                return None

            else:
                console.print(f"\nYour selection is not on the list. \nPlease choose a number between 1 and {len(current_list)}\n")
                logger.warning(f"Invalid {subject} option. Input is out of range.")
                continue

        except ValueError:
            console.print("\nPlease enter a valid number.\n")
            logger.warning(f"Invalid {subject} option. Input is not an integer.")
            continue





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



### DELETE

def select_movie(movielist):
    while True:
        console.print("Choose a movie by entering its number. \nEnter 0 to return to the main menu.\n")
        choice = int(console.input("[bold on #800000]Number:[/] "))

        try:
            if 1 <= choice <= len(movielist):
                selected_movie = movielist[choice - 1]
                console.print(f"Chosen movie: {selected_movie.get("title")}")
                logger.info(f"User selected movie '{selected_movie.get("title")}'.")
                return selected_movie, choice - 1
            elif choice == 0:
                return None, None
            else:
                console.print("\nYour selection is not on the list. Please try again.\n")
                logger.warning("Invalid movie option. Input is out of range.")
                continue
        except ValueError:
            console.print("\nPlease enter a valid number.\n")
            logger.warning("Invalid movie option. Input is not an integer.")
            continue