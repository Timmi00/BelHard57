# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.


def scramble(s1, s2):
    for i in set(s2):
        if s2.count(i) > s1.count(i):
            return False
    return True


print(scramble('scriptingjava', 'javascript'))
