def user_pow(x):
    return x ** 2


def genius_gen(begin, end, func):
    i = 0
    while end > i:
        yield begin
        begin = func(begin)
        i += 1


print(list(genius_gen(2, 4, user_pow)))
