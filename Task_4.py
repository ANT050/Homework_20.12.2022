# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input("\nВведите число: "))

#Преобразование десятичного числа в двоичное
def transformation(num):
  new_list = ''
  if num == 0:
    new_list = num
    
  else:
    while num != 0:
      new_list = str(num%2) + new_list
      num //=2
  return new_list

transform = transformation(num)
print(f'{num} -> {transform}')