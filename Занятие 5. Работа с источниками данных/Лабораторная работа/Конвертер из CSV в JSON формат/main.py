# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    fieldnames = ("longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","median_house_value"
)

    with open(INPUT_FILENAME) as csvf:
        with open(OUTPUT_FILENAME, 'w', encoding='utf8') as jsonf:
       # with open(OUTPUT_FILENAME, 'w', encoding='utf8') as jsonf:
                csvReader = csv.DictReader(csvf,fieldnames)
                for rows in csvReader:
                    jsonfile = json.dump(rows, jsonf, indent=4)
                    jsonf.write('\n')


                #print(rows['longitude'], rows['latitude'],rows['housing_median_age'],rows['total_rooms'],rows['total_bedrooms'],rows['population'],rows['households'],rows['median_income'],rows['median_house_value'])

    ...  # TODO Сериализовать в файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
