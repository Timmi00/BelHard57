#Заполнить список степенями числа 2 (от 2^1 до 2^n)
N_count = int(input())
print([2**i for i in range(1, N_count+1)])
