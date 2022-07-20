# 2. Вывести в порядке возрастания цифры, входящие в десятичную запись натурального числа N.
# n = str(input())
# list_numbers: list[int] = []
# while n + 1 // 10:
#     list_numbers.append(n % 10)
#     n //= 10
# print((sorted(str(list_numbers))))
print(sorted(set(input())))
