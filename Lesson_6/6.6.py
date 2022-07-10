# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
from random import randint
list_numbers: list[int] = [randint(1, 10000) for i in range(10)]
print(list_numbers)
for count in range(0, len(list_numbers)):
    if list_numbers[count] % 2 == 0:
        list_numbers.insert(0, list_numbers.pop(count))
    count -= 1
print(list_numbers)
