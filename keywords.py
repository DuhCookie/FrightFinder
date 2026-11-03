from api import get_keywords
from helpers import header, create_numerated_list


def ask_keyword():
    header("SEARCH KEYWORD")
    print("What kind of horror movie are you looking for?")
    keyword = input("Enter a keyword, theme or topic to get started: ")
    return keyword

def show_keywords(keywords=dict):
    if not keywords:
        print("\nThere are no available keywords found based on your entry. Please try again.")
        return None
    else:
        header("FOUND KEYWORDS")
        create_numerated_list(keywords, "name")
        # for index, result in enumerate(keywords, start=1):
        #     print(f"{index}. {result.get('name').capitalize()}")
        return "Found"

def select_keyword(keywords=dict):
    while True:
        print("\nChoose a keyword by entering its number. \nEnter 0 to search for another keyword.")
        choice = int(input("Number: "))

        if  1 <= choice <= len(keywords):
            selected = keywords[choice - 1]
            selected_id = selected.get("id")
            selected_keyword = selected.get("name").capitalize()
            print(f"Chosen keyword: {selected_keyword}")
            return selected_id, selected_keyword
        elif choice == 0:
            return None
        else:
            print("\nYour selection is not on the list. Please try again.")
            continue

def search_keyword():
    """
    Prompts the user to search for and select a keyword.
    :return:
    """
    while True:
        user_keyword = ask_keyword()
        received_keywords = get_keywords(user_keyword)

        result = show_keywords(received_keywords)
        if result is None:
            continue
        result = select_keyword(received_keywords)
        if result is None:
            continue

        selected_id, selected_keyword = result
        return selected_id, selected_keyword