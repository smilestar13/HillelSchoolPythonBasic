def common_elements(end_3, end_5):
    import random

    lst_3 = []
    lst_5 = []

    for i in range(random.randrange(end_3, end_3 + 1)):
        lst_3.append(random.randrange(0, 1_000, 3))
        lst_3 = lst_3[:end_3]
    for i in range(random.randrange(end_5, end_5 + 1)):
        lst_5.append(random.randrange(0, 1_000, 5))
        lst_5 = lst_5[:end_5]

    lst_3 = set(lst_3)
    lst_5 = set(lst_5)
    set_final = lst_3.intersection(lst_5)

    return set_final


x = int(input('Количество чисел кратное 3 (0:1000): '))
y = int(input('Количество чисел кратное 5 (0:1000): '))

print(common_elements(x, y))
