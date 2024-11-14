# TODO Напишите функцию find_common_items

def find_common_items(last, current):
    a = set(last)

    b = set(current)

    c = list(a.intersection(b))
    c.sort()
    return c




last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
