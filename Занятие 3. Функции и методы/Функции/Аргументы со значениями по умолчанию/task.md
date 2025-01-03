# Аргументы со значениями по умолчанию

## Цель урока:
После прохождения этого урока вы научитесь использовать аргументы со значениями по умолчанию в функциях Python.

### Аргументы со значениями по умолчанию
Аргументы со значениями по умолчанию — это аргументы функции, для которых заданы значения, которые будут использоваться, если вызывающая сторона не предоставляет соответствующие значения при вызове функции.

### Объявление функции с аргументами по умолчанию
Для объявления функции с аргументами по умолчанию используется следующий синтаксис:
```python
def function_name(arg1, arg2="default_value"):
    ... # тело функции
```
В данном примере `arg2` имеет значение "default_value" по умолчанию.


### Примеры вызова функции с аргументами по умолчанию
```python
def say_hello(name="World"):
    print(f"Hello, {name}!")

say_hello()  # Hello, World!
say_hello("User")  # Hello, User!
```

### Не рекомендуется использовать изменяемые типы данных
Не рекомендуется использовать изменяемые типы данных, такие как списки или словари, в качестве значений по умолчанию.  
Это связано с особенностями работы с изменяемыми объектами в Python.  
Вместо этого рекомендуется использовать значение `None` в качестве значения по умолчанию и внутри функции присваивать новое значение.
```python
# Плохой пример
def append_to_list(my_list=[]):
    ...
```
```python
# Хороший пример
def append_to_list(my_list=None):
    if my_list is None:
        my_list = []
    ...
```

### Важно отметить
Важно понимать, что позиционные и именованные аргументы, а также аргументы со значениями по умолчанию не связаны между собой.  
Кроме того, аргументы по умолчанию не влияют на порядок передачи остальных аргументов.
В функции можно передавать:
1. только позиционные аргументы, при этом не переопределяя значения по умолчанию;
2. как позиционные так и именованные, главное, чтобы сначала шли все позиционные, а затем именованные аргументы;
3. все позиционные аргументы, при этом важен порядок значений;
4. все именованные аргументы, при этом не важен порядок значений;