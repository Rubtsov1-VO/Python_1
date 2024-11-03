# TODO реализовать функцию count
def count(list_, int_):
    count = 0
    for i in list_:
        if int_ == i:
            count+=1
        else:
            continue
    return count


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
