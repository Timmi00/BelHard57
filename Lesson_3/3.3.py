#Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами.
f_name: str = input('введите своё имя: ')
age = int(input('введите свой возраст: '))
city: str = input('Ввендите свой город: ')
print('Меня зовут %s. Мне %d лет. Я из города %s.' % (f_name, age, city))
print('Меня зовут {}. Мне {} лет. Я из города {}.'.format(f_name, age, city))
print('Меня зовут {name}. Мне {age} лет. Я из города {city}.'.format(name=f_name, age=age, city=city))
print(f'Меня зовут {f_name}. Мне {age} лет. Я из города {city}.')