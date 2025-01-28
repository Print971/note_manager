# Функция для проверки, что строка не пустая и содержит хотя бы 3 символа
def is_valid_input(input_str, min_length=3):
    return len(input_str.strip()) >= min_length

# Запрашиваем у пользователя информацию для создания заметки
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Создаем список для хранения заголовков заметки
titles = []

# Бесконечный цикл для ввода заголовков заметки
while True:
    enter_title = input('Введите заголовок заметки (Для завершения нажмите Enter): ')
    if enter_title.strip() == '':
        break
    elif not is_valid_input(enter_title):
        print("Ошибка: Заголовок должен содержать хотя бы 3 символа. Попробуйте снова.")
    else:
        titles.append(enter_title)

# Выводим все данные заметки
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
print("Заголовки заметки:")
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")
