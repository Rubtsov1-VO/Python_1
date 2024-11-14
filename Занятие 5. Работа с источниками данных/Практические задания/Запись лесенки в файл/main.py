INPUT_FILE = "input.txt"


OUTPUT_FILE = "output.txt"
i = 0

def task():
    with open(OUTPUT_FILE, 'w') as f:
        for i in range(1,11):
            f.write(i * '*' + '\n')
# TODO построчно записать лесенку в файл


if __name__ == '__main__':
    # Необходимо для проверки
    task()
    with open(OUTPUT_FILE, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
