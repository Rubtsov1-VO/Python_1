number = 2342354235235

list_digits = [int(n) for n in str(number)]  # TODO c помощью list comprehension получить список цифр числа

print(sum(list_digits))  # TODO найти сумму цифр числа
print(sum([int(n) for n in str(number) if int(n)%2==0]))  # TODO найти сумму всех четных чисел
print(len(list_digits))  # TODO найти количество цифр
print(min(list_digits))  # TODO найти минимальную цифру
print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
