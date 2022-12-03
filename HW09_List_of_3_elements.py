import random
list_1 = []
list_2 = []

for i in range(random.randint(3, 10)):
    list_1.append(random.randint(1, 1_000))
print('Рандомный список', list_1)

list_2.append(list_1[0])
list_2.append(list_1[2])
list_2.append(list_1[-2])

print('Структурированный список', list_2)
