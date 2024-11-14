# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    summ = 0
    with open(FILENAME, 'r', encoding='utf8') as f:
        json_data = json.load(f)
    for i in json_data:
        p = i["score"] * i["weight"]
        summ += p
    return round(summ, 3)
print(task())
