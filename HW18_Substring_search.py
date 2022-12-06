def second_index(user_sent, find_ind):
    if user_sent.count(find_ind) > 1:
        str_fin = user_sent.find(find_ind)
        str_fin = user_sent.find(find_ind, str_fin + 1)
        return str_fin
    else:
        str_fin = None
        return str_fin


x = input('Enter your sentence: ')
y = input('Enter the desired index: ')

print(f'Your index number is {second_index(x, y)}.')
