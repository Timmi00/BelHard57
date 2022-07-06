#Заполнить список степенями числа 2 (от 2^1 до 2^n)
n_count = int(input())
print([2**i for i in range(1, n_count+1)])
