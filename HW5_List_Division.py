lst_0 = [1, 2, 3, 4, 5, 6]

y = len(lst_0)
x = y // 2

if x % 2:  # если четное количество символов
    lst_1 = (lst_0[0:x])
    lst_2 = (lst_0[x:y])

    res = [
        lst_1,
        lst_2
    ]
    print(res)
else:
    x += 1
    lst_1 = (lst_0[0:x])
    lst_2 = (lst_0[x:y])

    res = [
        lst_1,
        lst_2
    ]
    print(res)
