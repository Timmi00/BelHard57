# **Вывести четные числа от 2 до N по 5 в строку
try:
    number_n = int(input('Введите число: '))
except ValueError:
    number_n = int(input('Ведите число, а не строку: '))
start_number = 2
count: int = 0
while number_n:
    if count == 5:
        print('\n')
        count = 0
    if not start_number % 2 and number_n > 1:
        print(start_number, end=' ')
        start_number += 1
        count += 1
        number_n -= 1
    else:
        number_n -= 1
        start_number += 1
