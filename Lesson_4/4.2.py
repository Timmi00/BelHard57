# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

User_string = str((input().upper()))
print({User_string[i]: User_string.count(User_string[i]) for i in range(0, len(User_string))})

