# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
import re
Some_list = str((input().upper()))
# Dict_for_letters = {}
# for n in Some_list:
#     if n not in Dict_for_letters:
#         Dict_for_letters[n] = 1
#     else:
#         Dict_for_letters[n] += 1
Count: int = len(Some_list)
Dict_for_letters = {Some_list[i]: len(re.findall(Some_list[i], Some_list)) for i in range(0, Count)}
print(Dict_for_letters.items())
