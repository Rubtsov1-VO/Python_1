def count_powerful_powerplants(powerplants_list, threshold):
    count = 0      # TODO Найдите количество электростанций, мощность которых превышает заданное значение
    for key in powerplants_list:
        if key["power"] >= threshold:
            count+=1
        else:
            continue
    return count
powerplants = [
    {"name": "ГЭС-1", "power": 1200},
    {"name": "АЭС-2", "power": 3200},
    {"name": "ТЭЦ-3", "power": 2800},
    {"name": "СГУ-4", "power": 500},
    {"name": "ВЭС-5", "power": 1800},
]

threshold_power = 2000

powerplants_count = count_powerful_powerplants(powerplants, threshold_power)  # TODO Вызовите функцию count_powerful_powerplants
print(f"Количество электростанций, мощность которых превышает заданное значение: {powerplants_count}")
