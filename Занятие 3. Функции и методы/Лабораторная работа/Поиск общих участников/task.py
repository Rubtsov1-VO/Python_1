# TODO Напишите функцию find_common_participants



def find_common_participants(first, second,sep=","):
    list_ = []
    a = first.replace("|", sep).split(sep)
    b = second.replace("|", sep).split(sep)
    print(a,b)
    for i in b:
        if i in a:
            list_ += i.split(sep)
    return list_



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group))