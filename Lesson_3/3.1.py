#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
user_string: str = input()
print('Методом .replace : \n', user_string.replace(' ', '-'))
print('Методом .split и .join:\n', '-'.join(user_string.split()))
