x = input('Hi, input your number: ')

while x.isdigit:

    if '0' in x:
        print('Your final digit: 0')
        break
    else:
        res = eval(x.replace('', ' ').strip().replace(' ', ' * '))
        x = str(res)
        if len(x) > 1:
            continue
        else:
            print('Your final digit:', res)
            break
