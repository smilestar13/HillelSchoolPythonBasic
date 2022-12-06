def correct_sentence(str_start):
    str_fin = str_start[0].upper() + str_start[1:]
    if str_start[-1] == '.':
        return str_fin
    else:
        str_fin = str_fin + '.'
        return str_fin


user_sent = input('Enter your sentence: ')
print(f'=> {correct_sentence(user_sent)}')
