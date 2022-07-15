# You will be given an array of numbers. You have to sort the odd numbers in ascending order while
# leaving the even numbers at their original positions.
def sort_array(source_array):
    odd_numb = sorted([n for n in source_array if not n % 2 == 0])
    index = 0
    result = []
    for i in source_array:
        if not i % 2 == 0:
            result.append(odd_numb[index])
            index += 1
        else:
            result.append(i)
    return result


print(sort_array([5, 3, 1, 8, 0]))
