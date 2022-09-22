
def josephus(items, k):
    result = []
    n = 0
    while len(items):
        n = (n + k - 1) % len(items)
        print(n)
        result.append(items.pop(n))
    return result

print(josephus([1,2,3,4,5,6,7,8,9,10],3))
