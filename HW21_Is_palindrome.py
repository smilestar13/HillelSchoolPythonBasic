import string


def is_palindrome(str_a):
    str_a = str_a.lower().replace(' ', '')

    for el in string.punctuation:
        str_a = str_a.replace(el, '')

    str_b = str_a[::-1]

    return str_a == str_b


print(is_palindrome('A man, a plan, a canal: Panama'))
