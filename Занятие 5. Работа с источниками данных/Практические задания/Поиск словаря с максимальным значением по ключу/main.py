import json


FILENAME = "input.json"


def task() -> dict:

    i = 0
    with open(FILENAME, encoding='utf8') as f:
        file = json.load(f)
    ...  # TODO найти максимальный элемент по ключу score
    return max(file, key=lambda x: x["score"])

if __name__ == '__main__':
    print(task())
