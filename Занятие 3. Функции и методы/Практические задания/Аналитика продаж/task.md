# Аналитика продаж

Вы работаете аналитиком в компании, которая занимается анализом данных о продажах различных товаров.  
Вам поставлена задача разработать функцию для расчета общей стоимости проданных товаров за определенный период времени.

## Задача:
Напишите функцию `calculate_total_sales`, которая принимает на вход список словарей `sales_list`, где каждый словарь представляет информацию о продажах одного товара.  
Каждый словарь содержит следующие ключи:
- `"product"`: название товара,
- `"quantity"`: количество проданных единиц товара,
- `"price_per_unit"`: цена за одну единицу товара.

Функция должна рассчитать общую стоимость проданных товаров, умножив количество проданных единиц товара на цену за единицу и суммируя результаты для всех товаров в списке.  
Результат должен быть возвращен из функции.

<div class="hint">
  Чтобы найти общую стоимость проданных товаров необходимо пройти по каждому словарю в списке и рассчитать стоимость продажи каждого товара, умножая количество проданных единиц на цену за единицу товара.
</div>
