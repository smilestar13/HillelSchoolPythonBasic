print('Вас приветствует простейший калькулятор, ниже Вы сможете ввести 2 числа и выбрать как их обчислить. Удачи!')
print()

num_1 = float(input('Введите число-1:'))

action_1 = input('Выберите действие из предложенных (/, *, +, -):')

num_2 = float(input('Введите число-2:'))

if action_1 == '/' and num_2 != 0:
    print(num_1/num_2)
elif action_1 == '*':
    print(num_1*num_2)
elif action_1 == '+':
    print(num_1+num_2)
elif action_1 == '-':
    print(num_1-num_2)
else:
    print('На ноль делить нельзя!')
