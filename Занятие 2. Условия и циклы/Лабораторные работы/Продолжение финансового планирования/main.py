

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

common = spend - salary

i = 1
while True:
    common = common +  spend
    if i >= 9:
        break
    elif i < 9:
        common = common + (spend * 0.03) - salary
        i+=1


        # TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", common)
