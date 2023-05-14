'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Input:
1, 3, 7, 10, 5, 8
4
8
Output:
2(7), 4(5), 5(8)'''

my_list = [int(x) for x in input("Введите строку с числами: ").replace(",", " ").split()]
min_number = int(input("Минимум: "))
max_number = int(input("Максимум: "))
print(*(f"{i}({my_list[i]})" for i in range(len(my_list)) if min_number <= my_list[i] <= max_number), sep=", ")