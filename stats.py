def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter +=1
    return counter


def count_symbols(text):
    words_dict = {}
    low_text = text.lower()
    words_list = low_text.split()
    words_set = set(words_list)
    for word in words_list:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    test = words_dict
    return test