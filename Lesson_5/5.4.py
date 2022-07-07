# Вводится строка, определить количество пар одинаковых символов рядом стоящих в строке (не пересекающиеся вхождения)
user_string = input('Введите строку:')
res_dict: dict = {}
count: int = 0
res_str: str = ''
for i in range(len(user_string) - 1):
    if user_string[i] == user_string[i + 1]:
        res_str = user_string[i] + user_string[i+1]
        count += user_string.count(res_str)
        user_string = user_string[:i] + user_string[i + 2:]
print('Количество повторений: ', count)
