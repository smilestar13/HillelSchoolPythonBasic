def is_even_pro(num):
    num = int(str(num)[-1])
    x = list(range(0, 9, 2))
    return num in x


print(is_even_pro(2494563894038**2))
