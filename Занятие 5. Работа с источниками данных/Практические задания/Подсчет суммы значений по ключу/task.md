# Подсчет суммы значений по ключу

### Описание

Вы работаете над анализом данных о пользовательском опыте и имеете файл `input.json`, содержащий список словарей.  
Вам необходимо считать содержимое файла `input.json` и вычислить сумму значений по ключу `"contains_improvement_appeals"`. 

### Задачи

1. Откройте файл `input.json` и используя модуль `json` десериализайте его содержимое объект Python.
2. Пройдитесь по каждому словарю в списке и для каждого словаря получите значение по ключу `"contains_improvement_appeals"`.
3. Суммируйте полученные значения и верните результат в функции `task`.

<div class="hint">
  Для суммирования используйте list comprehension и встроенную функцию `sum`.
</div>
