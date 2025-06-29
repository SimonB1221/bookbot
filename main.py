from stats import count_words
from stats import count_symbols
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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