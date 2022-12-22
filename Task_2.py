# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math
import random
from random import randint

list_length = int(input("\nВедите длину списка: "))

# Создание списка
def initial_list(list_length):
    rand_list = []
    for i in range(list_length):
        rand_list.append(random.randint(0, 10))
    return rand_list

# произведение пар чисел (первое*последне, второе*предпоследнее ...)
def multiply_list(ferst_list):
    new_list = []
    for i in range(math.ceil(len(ferst_list)/2)):
        new_list.append(ferst_list[i]*ferst_list[len(ferst_list)-i-1])
    return new_list

ferst_list = initial_list(list_length)
multiply = multiply_list(ferst_list)
print(f'{ferst_list} => {multiply}')
