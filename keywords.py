from api import get_keywords
from helpers import header, create_numerated_list, create_table, select_from_list

from rich.console import Console
console = Console(force_terminal=True, legacy_windows=False, highlight=False)

def ask_keyword():
    header("SEARCH KEYWORD")
    print("\nWhat kind of horror movie are you looking for?")
    keyword = input("Enter a keyword, theme or topic to get started: ")
    return keyword

def show_keywords(keywords=dict):
    if not keywords:
        print("\nThere are no available keywords found based on your entry. Please try again.")
        return None
    else:
        header("FOUND KEYWORDS")
        keyword_table = create_table(None, keywords, False, "name")
        console.print(keyword_table)
        return "Found"

def search_keyword():
    """
    Prompts the user to search for and select a keyword.
    :return: The selected keyword ID and keyword name.
    """
    while True:
        user_keyword = ask_keyword()
        received_keywords = get_keywords(user_keyword)

        result = show_keywords(received_keywords)
        if result is None:
            continue
        result = select_from_list(received_keywords, "keywords")
        if result is None:
            continue

        selected_id, selected_keyword = result
        return selected_id, selected_keyword
