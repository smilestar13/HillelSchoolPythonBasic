import string


def first_word(str_a):
    string.punctuation = string.punctuation.replace("'", '')
    for el in string.punctuation:
        str_a = str_a.replace(el, ' ')
    str_a = str_a.split()[0]
    return str_a


print(first_word("... and so on ..."))
