# Поиск студентов по фамилии

### Описание
Вы являетесь администратором университетской базы данных студентов и вам необходимо реализовать алгоритм поиска студентов по фамилии.  
В базе данных хранится список студентов, где каждый студент представлен в виде словаря с ключами "имя" и "фамилия".  
Вам необходимо написать функцию, которая будет принимать фамилию в качестве аргумента и возвращать `True`, если студент с такой фамилией присутствует в базе, `False`, в противном случае.

### Задача
1. Напишите функцию `exists_student_by_lastname`, которая принимает два аргумента: 
   `students` (список словарей студентов) и `lastname` (фамилия для поиска).
2. Итерируйтесь по каждому студенту в списке `students`.
3. Проверьте, равна ли текущая фамилия студента заданной фамилии.
4. Если фамилии совпадают, верните `True`. Если пройдя весь список, не найдено ни одной фамилии, то вернуть `False`.
