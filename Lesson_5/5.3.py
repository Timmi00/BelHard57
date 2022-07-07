# **Вывести четные числа от 2 до N по 5 в строку
try:
    number_n = int(input('Введите число: '))
except ValueError:
    number_n = int(input('Ведите число, а не строку: '))
# start_number = 0
# count: int = 0
# while number_n:
#     if count == 5:
#         print('\n')
#         count = 0
#     if number_n < 2:
#         break
#     start_number += 2
#     print(start_number, end=' ')
#     number_n -= 2
#     count += 1
count_int: int = 0
for i in range(2, number_n + 1, 2):
    count_int += 1
    print(i, end=' ')
    if count_int == 5:
        print('\n')
        count_int = 0
