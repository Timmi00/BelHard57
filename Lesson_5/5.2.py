# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
try:
    number_1 = int(input('Введите первое число: '))
except ValueError:
    number_1 = int(input('введите число: '))
operation = input('Введите действие: ')
try:
    number_2 = int(input('Введите второе число: '))
except ValueError:
    number_2 = int(input('введите число:'))
if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == '/':
    print(number_1 / number_2)
elif operation == '**':
    print(number_1 ** number_2)
elif operation == '%':
    print(number_1 % number_2)
elif operation == '//':
    print(number_1 // number_2)
else:
    print('Вы ввели неправильное действие')
