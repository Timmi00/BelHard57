def digital_root(n):
    sum_n = 0
    while n:
        sum_n += n % 10
        n //= 10
    if sum_n > 9:
        return digital_root(sum_n)
    else:
        return sum_n


print(digital_root(12345))
