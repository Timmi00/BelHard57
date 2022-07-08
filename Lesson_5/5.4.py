# Вводится строка, определить количество пар одинаковых символов рядом стоящих в строке (не пересекающиеся вхождения)
user_string = input('Введите строку:')
count_non_intersecting: int = 0
i: int = 0
while i < len(user_string) - 1:
    if user_string[i] == user_string[i + 1]:
        count_non_intersecting += 1
        if user_string[i + 1] == user_string[i + 2]:
            i += 2
        else:
            i += 1
    else:
        i += 1
print('Общее количество повторений: ', count_non_intersecting)
