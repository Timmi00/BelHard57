# Вывести первые N чисел кратные M и больше K
number_n: int = int(input('Введите N '))
number_m = int(input('Введите M '))
number_k = int(input('Введите K '))
print('Первые ', number_n, 'чисел кратных',number_m, 'больше', number_k, ' :')
i = number_k - (number_k % number_m)  # Для быстрого отсеивания неподходящих чисел.
while number_n:
    if i > number_k and i % number_m == 0:
        print(i, end=' ')
        i += number_m
        number_n -= 1
    else:
        i += number_m
