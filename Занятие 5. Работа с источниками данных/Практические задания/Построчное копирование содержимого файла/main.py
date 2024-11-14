INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой
    with open(INPUT_FILE, 'r', encoding='utf8') as inn:
        with open(OUTPUT_FILE, 'w', encoding='utf8') as out:
            for i in inn:
                out.write(i.upper())

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for current_line in file:
            print(current_line, end="")
