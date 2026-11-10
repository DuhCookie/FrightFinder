from api import get_keywords
from helpers import header, create_table, select_from_list, console
from logger import logger


def ask_keyword():
    """
    Prompts the user to enter a keyword for a movie search.
    :return: The keyword entered by the user.
    """
    header("SEARCH KEYWORD")
    print("\nWhat kind of horror movie are you looking for?")
    keyword = input("Enter a keyword, theme or topic to get started: ")
    logger.info(f"User entered keyword: '{keyword}'.")
    return keyword

def show_keywords(keywords):
    """
    Displays the found keywords.
    :param keywords: A list of dictionaries containing the found keywords.
    :return: 'found' if keywords were found, otherwise None.
    """
    if not keywords:
        print("\nThere are no available keywords found based on your entry. Please try again.")
        logger.warning("No keywords were found.")
        return None
    else:
        header("FOUND KEYWORDS")
        keyword_table = create_table(None, keywords, False, "name")
        console.print(keyword_table)
        return "found"

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
