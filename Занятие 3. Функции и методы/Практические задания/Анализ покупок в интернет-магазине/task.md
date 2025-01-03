# Анализ покупок в интернет-магазине

### Описание
Вы работаете аналитиком в интернет-магазине и вам необходимо провести анализ покупок пользователей.  
В базе данных интернет-магазина хранятся списки покупок пользователей за два разных периода: за прошлую неделю и за текущую неделю.  
Вам необходимо найти товары, которые были куплены пользователями в обоих периодах, чтобы выявить наиболее популярные продукты.

### Задача
1. Напишите функцию `find_common_items`, которая принимает два списка товаров в качестве аргументов: `last_week_purchases` и `current_week_purchases`.
2. С помощью метода множества `intersection` найдите общие элементы среди списков `last_week_purchases` и `current_week_purchases`.
3. Отсортируйте общие товары в алфавитном порядке и верните результат в виде списка.

<div class="hint">
  Для того найти пересечение не обязательно приводить обе коллекции к множеству.
</div>
