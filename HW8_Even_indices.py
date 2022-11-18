lst_1 = [1, 3, 5]
print('Начальный список', lst_1)

x = len(lst_1)

if x > 1:
    a = lst_1[-1]
    lst_2 = lst_1[::2]
    i = (sum(lst_2))
    print('Ответ:', i * a)
elif x == 1:
    a = lst_1[-1]
    print('Ответ:', a*a)
else:
    print('Ответ: 0')
