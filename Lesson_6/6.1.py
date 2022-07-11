# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
user_number = int(input())


def dec_bin_dec(num):
    number_bin = ''
    number_dec = 0
    while num:
        number_bin = str(num % 2) + number_bin
        num = num // 2
    # for i in range(0, len(number_bin)):
    #     number_dec = number_dec + int(number_bin[i]) * (2 ** (len(number_bin) - i - 1))
    return number_bin


print(dec_bin_dec(user_number), user_number)
