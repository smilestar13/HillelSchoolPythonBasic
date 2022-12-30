def prime_generator(break_num):
    i = 2
    while i < break_num:
        prime_num = True
        for num in range(2, i):
            if i % num == 0:
                prime_num = False
                break
        if prime_num:
            yield i
        i += 1


print(list(prime_generator(100)))
