# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from random import randint, uniform

list_length = int(input("\nВедите длину списка: "))

# Создание списка
def initial_list(list_length):
    new_list = []
    for i in range(list_length):
        new_list.append(round(uniform(1, 99), randint(0, 2)))
    return new_list

#Создание нового списка дробных чисел за минусов нулевых значений
def fractional_part(ferst_list):
    new_list = []
    for i in range(len(ferst_list)):
        if ferst_list[i]%1 > 0:
            new_list.append(round(ferst_list[i]%1, 2))
    return new_list
  
#Разница между максимальным и минимальным элементами
def difference_max_min(second_list):
  for i in range(len(second_list)):
    diff = max(second_list) - min(second_list)
  return diff

ferst_list = initial_list(list_length)
second_list = fractional_part(ferst_list)
difference = difference_max_min(second_list)

print(f'{ferst_list} => {round(difference, 2)}')

