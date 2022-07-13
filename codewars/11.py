# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    # result_string = ''
    # for n in sorted(a1 + a2):
    #     if n not in result_string:
    #         result_string += n
    # return result_string
    return "".join(sorted(set(a1 + a2)))

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))