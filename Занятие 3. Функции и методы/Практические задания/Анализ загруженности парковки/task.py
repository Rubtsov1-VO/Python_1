# TODO Напишите функцию `calculate_parking_load`
def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):
    if total_parking_spaces >= occupied_parking_spaces and total_parking_spaces > 0 and occupied_parking_spaces > 0:
        common = round(occupied_parking_spaces/ total_parking_spaces * 100)
        return common

total = calculate_parking_load(10, 3)

print(total)