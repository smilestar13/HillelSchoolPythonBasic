def add_one(a):
    a = int(''.join(map(str, a))) + 1
    result = []
    while a > 0:
        result.append(a % 10)
        a //= 10
        result.reverse()
    return result


lst_1 = [9, 9, 9, 9]
print(add_one(lst_1))
