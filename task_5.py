# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

num = int(input('\nВведите число: '))
fibo = [1, 1]
negofibo = [1, -1]

for i in range(2, num):
    element_fib = fibo[i-1]+fibo[i-2]
    fibo.append(element_fib)

    element_negofib = negofibo[i-2] - negofibo[i-1]
    negofibo.append(element_negofib)

fibo.insert(0, 0)
negofibo.reverse()

print(f'\nДля k = {num} список будет выглядеть так:\n{negofibo+fibo}')
