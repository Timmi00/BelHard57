# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)


def morze(string):
    dict_for_letters = {' ': '   ', '1': '.----', '2': '..---', '3': "...--", '4': '....-', '5': '.....', '6': '-....',
                        '7': '--...', '8': '---..', '9': '----.',
                        'a': '.-', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
                        'i': '••',
                        'j': '•———',
                        'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
                        's': '•••',
                        't': '—',
                        'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}
    result_string: str = ''
    for i in string:
        result_string += dict_for_letters[i]+' '
    return result_string


user_string = input().lower()
print(morze(user_string))