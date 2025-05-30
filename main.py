import sys
from stats import get_num_words, get_char_counts, sort_char_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    # Check if the correct number of arguments is passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(text)
    sorted_chars = sort_char_dict(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
