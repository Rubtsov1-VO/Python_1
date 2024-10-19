from itertools import count

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0


summ = money_capital + salary - spend

while True:
    money_capital = summ + salary
    spend = spend + (spend * 0.05)
    if  summ <= 0:
        break
    elif summ > 0:
        summ = money_capital - spend
        count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
