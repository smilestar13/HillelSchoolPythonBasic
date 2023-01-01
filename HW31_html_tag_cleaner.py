import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    work_lst = []

    html_hh = codecs.open(html_file, 'r', 'utf-8').read()

    for el in html_hh:  # Закидываю каждый элемент в список
        work_lst.append(el)

    while work_lst.count('<'):  # Сношу все что между <>
        if '<' or '>' in work_lst:
            z = work_lst.index('<')
            t = work_lst.index('>')
            del work_lst[z:t + 1]
            continue
        if '<' or '>' not in work_lst:
            break

    html_hh = codecs.open('cleaned.txt', 'w', 'utf-8')  # Создаю новый пустой файл 'cleaned.txt'
    # work_lst = ''.join(work_lst).split('  ')  # Можно убрать отступы

    for txt in work_lst:  # Записываю результат без тегов в чистый .txt файл
        html_hh.write(txt)

    html_hh.close()
    return result_file


delete_html_tags("draft.html")
