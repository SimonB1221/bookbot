from stats import count_words
from stats import count_symbols
from stats import sort_list
import sys

if len(sys.argv) == 2:
    book = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    symbol_count = count_symbols(text)
    list = sort_list(symbol_count)
    for i in list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()