count: int = 0
while count == 0:
    word = input()
    if 'hello' != word:
        print('wrong')
    if 'hello' == word:
        count += 1
print('hello')
