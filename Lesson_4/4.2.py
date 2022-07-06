# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

user_string = str((input().upper()))
print({user_string[i]: user_string.count(user_string[i]) for i in range(0, len(user_string))})

