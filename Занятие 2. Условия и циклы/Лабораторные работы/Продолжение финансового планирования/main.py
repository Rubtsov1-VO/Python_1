

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


i=1
common = spend - salary
summ = 0
spend2 = 0
final = 0


while True:
    spend2 = spend + (spend2 * 0.03)
    if i < months:
        spend2 =  spend2 - salary
        spend += spend * 0.03
        i+=1
        #print(spend - salary)
        summ = spend - salary
        #print(summ)
    else:
        break
    final += summ
common = final + common

        # TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(common,2))
