# TODO реализовать функцию
def remove_whitespace(str_):
    a = str_.split(' ')

    b = []

    for i in a:
        if i:
            b.append(i)

    return ' '.join(b)
str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))



