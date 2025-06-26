import sys
from stats import get_book_text, count_words, count_characters, char_count_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    num_words = count_words(book_contents)
    char_counts = count_characters(book_contents)
    sorted_chars = char_count_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
