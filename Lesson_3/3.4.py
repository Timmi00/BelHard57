# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
positive: int = ((number1 > 0) + (number2 > 0) + (number3 > 0))
print(f'Положительных чисел: {positive}\nОтрицательных чисел: {3-positive}')
