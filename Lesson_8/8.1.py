# 1. Реализовать бинарный поиск элемента в отсортированном списке.
# Дан список чисел, пользователь вводит число, необходимо реализовать поиск
# введенного пользователем числа в этом списке с помощью бинарного поиска
def bin_search(list, n, start, end):
    if start > end:
        return False
    mid = int((start + end) / 2)
    if n == list[mid]:
        return True
    if n < list[mid]:
        return bin_search(list, n, start, mid - 1)
    else:
        return bin_search(list, n, mid + 1, end)


list_numbers: list[int] = [1, 12, 23, 34, 45, 56, 67, 78, 89]
n = int(input())
start = 0
end = len(list_numbers) - 1
print(bin_search(list_numbers, n, start, end))
