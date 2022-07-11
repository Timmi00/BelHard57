# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
user_dict: dict = {
    1: {"f_name": 'Timyr', "l_name": 'Tishkevich', "tel_number": '375299301835', "email": 'timmi00@tut.by'},
    99: {"f_name": 'Alex', "l_name": 'Coach', "tel_number": '375299999999', "email": 'coach@tut.by'},
    6: {"f_name": 'Dima', "l_name": 'Gocha', "tel_number": '37527654387'},
    3: {"f_name": 'Ivan', "l_name": 'Ivanov', "tel_number": '375299301835', 'email': 'python@python.py'},
    19: {"f_name": 'Vasya', "l_name": 'Tishkevich', "tel_number": '375299301835', "email": ''},
}
for key, value in user_dict.items():
    try:
        if not value["email"]:
            print(value['f_name'])
    except KeyError as exc:
        print(value['f_name'])
