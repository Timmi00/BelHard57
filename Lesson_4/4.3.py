# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
Name_email: [str] = str(input()).split(' ')
Name: list[str] = Name_email[:: 2]
Email: list[str] = Name_email[1::2]
Count: int = round(len(Name_email)/2)
# Dict_name_email = {}
# for i in range(0, len(Name)):
#     Dict_name_email[Name[i]] = Email[i]
# Dict_result = {}
# for n in range(0, len(Name)):
#     Dict_result[n] = Dict_name_email.popitem()
Dict_name_email = {Name[i]: Email[i] for i in range(0, Count)}
Dict_result = {i: Dict_name_email.popitem() for i in range(0, Count)}
print(Dict_result)
