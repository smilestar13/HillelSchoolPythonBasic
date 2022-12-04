x = input('Введите количество секунд для вычесления: ')

if x.isdigit():
    x = int(x)
    if 0 <= x <= 8639999:

        day, next = (x // (24 * 60 * 60), x % (24 * 60 * 60))
        hours, next = (next // (60 * 60), next % (60 * 60))
        minutes, seconds = (next // 60, next % 60)

        hours = hours.__str__().zfill(2)
        minutes = minutes.__str__().zfill(2)
        seconds = seconds.__str__().zfill(2)

        next, second_day = divmod(day, 10)

        if 2 <= second_day <= 4:
            count = 'дня'
        elif second_day == 1:
            count = 'день'
        else:
            count = 'дней'

        print(f'Результат вычесления: {day} {count}, {hours}:{minutes}:{seconds}')
    else:
        print('Wrong number!')
else:
    print('Print only number!')
