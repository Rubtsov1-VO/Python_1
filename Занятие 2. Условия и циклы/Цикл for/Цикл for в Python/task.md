# Урок: Цикл for в Python

## Цель урока:
После прохождения этого урока вы научитесь использовать цикл `for` в Python.

### Цикл `for`
Цикл `for` в Python используется для итерации (повторения) через последовательность или коллекцию элементов.  
Он позволяет выполнять определенный блок кода для каждого элемента в последовательности.

Синтаксис цикла `for`:
```python
for value in collection:
    # Начало блока кода с телом цикла
    ...
    ...
    ...
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла
```
где:
- `value` - название переменной, которое будет использовано внутри цикла. 
  Объявление это переменной немного отличается, дня неё не нужно использовать `=`.
- `collection` - коллекция элементов
В каждой итерации цикла значение переменной `value` будет меняться интерпретатором, принимая значение следующего элемента из последовательности `collection`.

Пример использования цикла `for`:
```python
for i in range(3):
    # Переменная `i` будет иметь новое значение внутри цикла на каждом шаге
    print(i+1, "шаг цикла")  # будет выполнено 3 раза
print("Первый цикл закончился!")
print()
```

В данном примере цикл `for` выполняется 3 раза, поскольку `range(3)` создает последовательность чисел от 0 до 2. 
Значение переменной `i` меняется на каждой итерации.

> Примечание: Старайтесь давать осмысленные названия переменным в цикле. Но можно использовать названия i и j, которые сложились исторически.  
> Их смысл будет понятен другим разработчикам. Например, i используется для перебора индексов

### Использование `_` в цикле
Если в цикле не требуется использовать значение переменной, вы можете заменить ее на символ `_`.  
Это позволяет сказать, что значение не требуется в данном контексте.

Пример использования `_` в цикле:
```python
for _ in range(5):  # Просто выполнить цикл 5 раз
    print("Hello World!!! :)")
```

В данном примере код внутри цикла будет выполняться 5 раз, но значение переменной не используется, поэтому оно заменено на `_`.

## Задание: Работа с циклом for
Запустите код и проанализируйте результат выполнения программы.