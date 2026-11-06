import random
import textwrap

from rich.console import Console
from rich.table import Table
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

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
    icon = get_icon()
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
        choice = console.input("[bold on #800000]Number:[/] ")

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
        choice = int(console.input("[bold on #800000]Number:[/] "))

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
    console.print(f"[bold]Title:[/] {title}\n")
    console.print(f"[bold]Summary:[/] {textwrap.fill(movie.get("overview"), width= 70)}\n")
    console.print(f"[bold]Rating:[/] {rating}")
    console.print(f"[bold]Release date:[/] {release_date}")
    console.print(f"[bold]Language:[/] {movie.get("original_language")}")

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