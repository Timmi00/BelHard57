# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
# of characters then it should replace the missing second character of the final pair with an underscore ('_')
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result


s = 'timyr'
print(solution(s))
