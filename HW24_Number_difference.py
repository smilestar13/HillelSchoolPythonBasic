def difference(*args):
    if not args:
        return 0
    else:
        res = max(*args) - min(*args)
        return res


print(round(difference(10.2, -2.2, 0, 1.1, 0.5), 2))
