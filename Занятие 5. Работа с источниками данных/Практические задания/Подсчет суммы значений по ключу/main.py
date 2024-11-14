import json


FILENAME = "input.json"


def task() -> int:
    g = 0
    ...  # TODO Десериализуйте содержимое JSON файла
    with open(FILENAME, encoding='utf8') as f:
        data = json.load(f)
    ...  # TODO Просуммируйте все значения по ключу contains_improvement_appeals
    for i in data:
        g += i["contains_improvement_appeals"]
    return g
if __name__ == '__main__':
    print(task())
