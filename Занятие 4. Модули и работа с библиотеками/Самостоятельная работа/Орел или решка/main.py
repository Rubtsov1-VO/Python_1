from random import choice, random

EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

count = 0
pob = []
c = 0
b = 0

for i in counts:
    while i > count:
        a = choice(coin)
        pob.append(a)
        count +=1
    for i in pob:
        if i == 'Решка':
            c +=1
        elif i == 'Орел':
            b +=1
    if c > b:
        d = b/c
    elif b >c:
        d = c/b
    elif b == c:
        d = b/c
    list_freq.append(d)

        # TODO подсчитать количество выпаданий орлов и решек


    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
