from keywords import search_keyword
from movies import discover_movie

def main():
    keyword_id, keyword = search_keyword()
    discover_movie(keyword_id, keyword)

main()
