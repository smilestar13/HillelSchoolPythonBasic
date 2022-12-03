import string

user_input = input('Введите две буквы через дефис: ')
x = user_input[0]
y = user_input[-1]

abc = list(string.ascii_letters)

in_1 = (abc.index(x))
in_2 = (abc.index(y) + 1)
res_lst = (abc[in_1:in_2])

res_str = "".join(res_lst)
print('Результат:', res_str)
