# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
from random import randint

list_length = int(input("\nВедите длину списка: "))

# Создание массива
def initial_list(list_length):
    rand_list = []
    for i in range(list_length):
        rand_list.append(random.randint(0, 10))
    return rand_list

#Нахождение суммы элементов с нечетным индексом
def sum_elements_odd_index(ferst_list):
    summa = 0
    for i in range(1, len(ferst_list), 2):
        summa += ferst_list[i]
    return summa

ferst_list = initial_list(list_length)
sum_elements = sum_elements_odd_index(ferst_list)
print(f'Сумму элементов списка {ferst_list}, стоящих на позиции с нечетным индексом = {sum_elements}')
