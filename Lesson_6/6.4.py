# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
user_list: list[any] = [True, 1, 'Hello', None, False, False, 'Python', None, 444, 'World']
count: int = len(user_list) - 1
while count -1 :
    print(user_list[count])
    if user_list[count] == str:
        del user_list[count]
        count -= 1
    else:
        count -= 1
print(user_list)

