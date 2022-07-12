#Find the missing letter
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.
def find_missing_letter(chars):
    lettter_case = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = lettter_case.find(chars[0])
    n = 0
    while lettter_case[i] == chars[n]:
        i += 1
        n += 1
    return lettter_case[i]


print(find_missing_letter('ABBS'))
