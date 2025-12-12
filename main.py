from stats import number_of_words,number_of_characters,make_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def sort_on(items):
    return items["num"]


def main(path):
    book = get_book_text(path)
    num_words = number_of_words(book)
    num_chars = number_of_characters(book)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    list_chars = make_list(num_chars)
    list_chars.sort(reverse = True, key = sort_on)
    for item in list_chars:
        print(f"- {item["char"]}: {item["num"]}")

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
