# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
user_list = [1, 2, 3, 4, 5, 6, 7]
shifts = int(input())
while shifts > len(user_list):
    shifts -= len(user_list)
num_for_slice = len(user_list) - shifts
print(user_list[num_for_slice:] + user_list[:num_for_slice])


def shift(lst, count):
    for i in range(count):
        lst.insert(0, lst.pop())
    return lst


print(shift(user_list, shifts))
