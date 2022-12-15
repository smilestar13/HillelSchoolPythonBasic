def popular_words(start_str, finders):
    start_str = start_str.lower()
    f_dict = {}
    for el in finders:
        el = f' {el} '
        if el in start_str:
            f_dict[el.strip()] = start_str.count(el)
        else:
            f_dict[el.strip()] = 0
    return f_dict


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
