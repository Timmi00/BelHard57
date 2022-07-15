# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n х m,
# заполнив ее по спирали числами от 1 до n x m.
# Спираль начинается в левом верхнем углу и закручивается по часовой стрелке.
n, m = int(input()), int(input())
matrix = [None] * n * m
x = (1, n, -1, -n)
y = 0
index = 0
count = n
for i in range(n * m):
    matrix[index] = i + 1
    if index == n * m - 1 or index == n - 1 or matrix[index + x[y]] or index == n * m - n:
        y = (y + 1) & 3
    index += x[y]
while m:
    print(matrix[n - count:n])
    n += count
    m -= 1
