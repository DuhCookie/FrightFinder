# Zoeken, filteren en randomizer

from helpers import header

def ask_keyword():
    header("SEARCH KEYWORD")
    print("What kind of horror movie are you looking for?")
    keyword = input("Enter a keyword, theme or topic to get started: ")
    return keyword

def show_keywords(keywords=dict):
    header("FOUND KEYWORDS")
    for index, result in enumerate(keywords, start=1):
        print(f"{index}. {result.get('name').capitalize()}")

def choose_keyword(keywords=dict):
    choice = int(input("\nChoose a keyword number: "))
    selected = keywords[choice - 1]
    selected_id = selected.get("id")
    selected_keyword = selected.get("name").capitalize()
    print(f"Chosen keyword: {selected_keyword}")

    return selected_id, selected_keyword

def discover_movie():
    pass