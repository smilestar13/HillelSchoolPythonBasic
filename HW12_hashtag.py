import string

user_input = input('Введите что вы хотите превратить в hashtag: ')

lst1 = list(user_input)
lst2 = []
lst3 = []

for el in lst1:
    if el in string.punctuation:
        lst2.append(el)
    else:
        lst3.append(el)

work_str = "".join(lst3)
work_str = work_str.title()
work_str = work_str.replace(' ', '')

if len(work_str) > 139:
    print(f'#{work_str[:139]}')
else:
    print(f'#{work_str}')
