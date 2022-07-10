# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
city_dict: dict = {
    'Belarus': ('Minsk', 'Vitebsk', 'Mogilev', 'Brest'),
    'Ukrain': ('Kiev', 'Rovno', 'Dnepr', 'Odessa'),
    'Bulgaria': ('Sofia', 'Varna'),
    'Turkey': ('Stambul', "Alanya", 'Ankara')
}
user_city = input().capitalize()
for key in city_dict:
    if user_city in city_dict.get(key):
        print(key)
        break
