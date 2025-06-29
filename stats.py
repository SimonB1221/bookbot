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
    return symbol_dict

def sort_on(dict):
    return dict["num"]

def sort_list(dict):
    list_of_dict = []
    for symbol in dict:
        key_pair = {"char": symbol, "num": dict[symbol]}
        list_of_dict.append(key_pair)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict