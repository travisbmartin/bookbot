from stats import word_count, char_count, char_sort
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        text = f.read()
        return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    words = word_count(text)
    char = char_count(text)
    sorted = char_sort(char)

    print("============ BOOKBOT ============")
    print("Analyzing book fount at bookes/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {words} total words.')
    print("--------- Character Count -------")

    for item in sorted:
        char = item["char"]
        count = item["count"]  # Access the character
        if char.isalpha():   # Skip non-alphabetical characters
            print(f'{char}: {count}')
    print("============= END ===============")

main()
