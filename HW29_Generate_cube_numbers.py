def generate_cube_numbers(start_num):
    i = 2
    while True:
        fin_num = i**3
        i += 1
        if start_num > fin_num:
            yield fin_num
        else:
            break


print(list(generate_cube_numbers(100)))
