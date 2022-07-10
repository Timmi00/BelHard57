# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
list_number: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_iter: int = len(list_number)
count_index = 0
while count_iter:
    list_number.insert(count_index, list_number.pop(len(list_number) - 1))
    count_iter -= 1
    count_index += 1
print(list_number)
