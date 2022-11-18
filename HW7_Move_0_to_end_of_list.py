lst_0 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print('Стартовый список:', lst_0)

lst_1 = []
lst_2 = []

for el in lst_0:
    if el == 0:
        lst_2.append(el)
    else:
        lst_1.append(el)

lst_1 += lst_2
print('Список с нулями в конце:', lst_1)
