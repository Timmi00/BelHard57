# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
list_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
count = -1
sum_result: list = []
while count < len(list_numbers) - 1:
    sum_result.append([list_numbers[count], (list_numbers[count - 1] + list_numbers[count + 1])])
    count += 1
print(sorted(sum_result))
