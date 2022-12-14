def find_unique_value(no_set):
    for el in no_set:
        if no_set.count(el) <= 1:
            return el


print(find_unique_value([2, 3, 3, 3]))
