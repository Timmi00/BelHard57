# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
Name_email = (input()).split(' ')
Name: list[str] = Name_email[:: 2]
Email: list[str] = Name_email[1::2]
Count: int = round(len(Name_email)/2)
print({i: {'Name': Name[i], 'Email': Email[i]} for i in range(0, Count)})
