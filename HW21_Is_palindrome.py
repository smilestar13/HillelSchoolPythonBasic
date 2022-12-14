import string


def is_palindrome(str_a):
    str_a = str_a.lower().replace(' ', '')
    lst_a = []

    for el in str_a:
        if el not in string.punctuation:
            lst_a.append(el)

    lst_b = lst_a[:]
    lst_b.reverse()

    if lst_a == lst_b:
        return True
    else:
        return False


print(is_palindrome('A man, a plan, a canal: Panama'))
