# Дан список чисел, в которым числа погут повторяться подряд несколько раз,
# необходимо реализовать алгоритм сжатия данного списка
# Пример: [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 1]
# Результат: [1, 5, 2, 8, 3, 2, 4, 2, 5, 1, 1, 1]

uncomp_list: list[int] = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 1, 2, 3, 2, 2, None]
comp_list: list[int] = []
count = 1
for number in range(len(uncomp_list) - 1):
    if uncomp_list[number] == uncomp_list[number + 1]:
        count += 1
    else:
        comp_list.append(uncomp_list[number])
        comp_list.append(count)
        count = 1
print(comp_list)
