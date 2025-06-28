def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter +=1
    return counter


def count_symbols(text):
    symbol_dict = {}
    low_text = text.lower()
    for character in low_text:
        if character in symbol_dict:
            symbol_dict[character] = symbol_dict[character] + 1
        else:
            symbol_dict[character] = 1
    test = symbol_dict
    return test