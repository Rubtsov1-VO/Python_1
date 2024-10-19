hour = 19

if 6 < hour <= 11:
    print("Утро")
elif 12 < hour <= 17:
    print("День")# TODO Реализуйте алгоритм при помощи условных операторов
elif 18 < hour <=23:
    print("Вечер")
elif 0 < hour < 5:
    print("Ночь")
else:
    print("Недопустимое количество часов")