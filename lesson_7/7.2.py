# Дано число, определить является ли оно простым
def enumeration_of_divisors(n):
    if n % 2 == 0 or n < 3:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


print(enumeration_of_divisors(int(input())))
