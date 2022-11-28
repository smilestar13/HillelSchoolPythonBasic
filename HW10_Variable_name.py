import string
import keyword

user_str = input('Введите имя переменной:')

x = user_str[0]

if user_str.isdigit():
    user_str = False
    print(user_str)
elif x.isdigit():
    print(False)
elif not user_str.islower() and user_str != '_':
    print(False)
elif user_str in keyword.kwlist:
    print(False)
else:
    res = True
    for sym in string.punctuation:
        if sym in user_str and sym != '_':
            res = False
    print(res)
