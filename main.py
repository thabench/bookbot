import sys
from stats import get_num_words, count_characters, sort_chars


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        file_text = f.read()
    return file_text


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath=filepath)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_chars = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()
