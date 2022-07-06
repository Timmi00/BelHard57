# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
List_name_email: [str] = str(input()).split(' ')
Name: list[str] = List_name_email[:: 2]
Email: list[str] = List_name_email[1::2]
Count: int = round(len(List_name_email)/2)
Dict_result = {i: {Name[i]: Email[i]}.popitem() for i in range(0, Count)}
print(Dict_result)
