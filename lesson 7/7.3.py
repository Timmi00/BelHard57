# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n х m,
# заполнив ее по спирали числами от 1 до n x m.
# Спираль начинается в левом верхнем углу и закручивается по часовой стрелке.
n, m, dx, dy, x, y = int(input()), int(input()), 0, 1, 0, 0
matrix = [[0] * m for _ in range(n)]
for i in range(1, n * m + 1):
    matrix[x][y] = i
    if matrix[(x + dx) % n][(y + dy) % m]:
        dx, dy = dy, -dx
    x += dx
    y += dy
for line in matrix:
    print(*(f'{i:<3}' for i in line), sep='')
