# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
Some_list = str((input().upper()))
Dict_for_letters = {}
for n in Some_list:
    if n not in Dict_for_letters:
        Dict_for_letters[n] = 1
    else:
        Dict_for_letters[n] += 1
print(Dict_for_letters.items())
