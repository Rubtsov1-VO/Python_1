# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]

for i in students:

    if int(i['grade']) > 3:
        print(i['name']+". Оценка:", i['grade'])  # TODO Распечатать имена студентов с оценками выше тройки
