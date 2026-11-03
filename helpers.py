import textwrap

def header(title):
    print()
    print("=" * len(title))
    print(title)
    print("=" * len(title))

def create_numerated_list(received_list, key):
    for index, result in enumerate(received_list, start=1):
        print(f"{index}. {result.get(key).capitalize()}")

def action_menu(movie_title, movie, watchlist=False):
    if watchlist:
        action = f"Remove {movie_title} from watchlist"
    else:
        action = f"Add {movie_title} to watchlist"

    while True:
        print("\nWhat would you like to do?")
        print(f"1. {action}")
        print("2. Go back")
        print("3. Return to main menu")
        choice = input("\nNumber: ")

        match choice:
            case "1":
                if watchlist:
                    return "remove"
                else:
                    return "add"
            case "2":
                return "back"
            case "3":
                return "main menu"
            case _:
                print("Invalid choice. Please try again")
                continue

def select_movie(movielist):
    while True:
        print("\nChoose a movie by entering its number. \nEnter 0 to return to the main menu.")
        choice = int(input("Number: "))

        if 1 <= choice <= len(movielist):
            selected_movie = movielist[choice - 1]
            print(f"Chosen movie: {selected_movie.get("title")}")
            return selected_movie, choice - 1
        elif choice == 0:
            return None
        else:
            print("\nYour selection is not on the list. Please try again.")
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
    print(f"Title: {title}\n")
    print(f"Summary: {textwrap.fill(movie.get("overview"), width= 70)}\n")
    print(f"Rating: {rating}")
    print(f"Release date: {release_date}")
    print(f"Original language: {movie.get("original_language")}")

    return title