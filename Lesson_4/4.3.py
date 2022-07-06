# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
# Name_email = (input()).split(' ')
# Count_words: int = len(Name_email)
# print({round(i/2): {'Name': Name_email[i], 'Email': Name_email[i+1]} for i in range(0, Count_words, 2)})
print({i: {'Name': input(), 'Email': input()} for i in range(0, int(input()))})
