from api import get_keywords
from movies import ask_keyword, show_keywords, choose_keyword


def main():
    user_keyword = ask_keyword()
    received_keywords = get_keywords(user_keyword)
    show_keywords(received_keywords)
    choose_keyword(received_keywords)

main()
