## Таблица умножения

### Описание

Математика является одним из фундаментальных навыков, который используется в повседневной жизни.  
Таблица умножения помогает быстро и легко выполнять умножение чисел.  
В этом задании вы создадите программу, которая распечатает таблицу умножения.

### Задача

1. Используйте два вложенных цикла `for` для создания таблицы умножения.
2. Установите диапазон первого цикла от 2 до 9 (включительно).
3. Во внутреннем цикле, также установите диапазон от 2 до 9 (включительно).
4. В каждой итерации внутреннего цикла, распечатайте результат умножения текущих значений обоих циклов.
5. Используйте форматирование f-строки для выравнивания значений в ячейках таблицы по левому краю до ширины 2.
6. После последнего столбца каждой строки не должно быть пробельных символов.

<div class="hint">
  Обычно внешний цикл используется для прохождения по строкам, а вложенный для прохождения по столбцам. Для индекса строки можно использовать переменную `i`, а для индекса столбца `j`. 
</div>

<div class="hint">
  При прохождении во вложенном цикле проверяйте, если это последний столбец, то значение `end` для функции `print` должно быть пустой строкой.
</div>
