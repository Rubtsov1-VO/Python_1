# Явное приведение типов в Python

## Цель урока:
В этом уроке вы узнаете о явном приведении типов в Python и научитесь преобразовывать данные из одного типа в другой.  
Рассмотрите примеры приведения строк к числам и различий между сложением строк и сложением чисел.

## Теория:

### Явное приведение типов
В Python можно явно приводить данные из одного типа в другой с помощью встроенных функций приведения типов.  
Это позволяет выполнять операции и работать с данными в нужном формате.

### Примеры приведения строки к числу
Часто возникает необходимость преобразовать строку, содержащую числовое значение, в число.  
Это может понадобиться, когда вы работаете с функцией `input`, которая всегда возвращает строки.
Для этого используются функции `int()` и `float()`. Например:

```python
num_str = "10"
num_int = int(num_str)  # Приведение строки к целочисленному типу
num_float = float(num_str)  # Приведение строки к типу с плавающей запятой
```

### Разница между сложением строк и сложением чисел
Если строки содержат числовые значения, то их сложение будет происходить как конкатенация строк, а не сложение чисел:
```python
num_str1 = "10"
num_str2 = "20"
result = num_str1 + num_str2  # "1020"
```

Чтобы выполнить сложение чисел, необходимо сначала привести строки к числовому типу:
```python
num_str1 = "10"
num_str2 = "20"
result = int(num_str1) + int(num_str2)  # 30
```

## Задание: Нахождение уникальных элементов

### Описание:
Найти количество уникальных символов в строке.

### Задача:
1. С помощью типа данных множества, найдите в строке `str_` уникальные символы.
2. Выведите количество уникальных символов в строке.
