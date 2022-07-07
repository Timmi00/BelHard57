# Вводится строка, определить количество пар одинаковых символов рядом стоящих в строке (не пересекающиеся вхождения)
user_string = input('Введите строку:')
res_dict: dict = {}
res_str: str = ''
for i in range(len(user_string) - 1):
    if user_string[i] == user_string[i + 1]:
        res_str = user_string[i] + user_string[i+1]
        res_dict.setdefault(res_str, user_string.count(res_str))
print('Общее количество повторений: ', sum(res_dict.values()))
