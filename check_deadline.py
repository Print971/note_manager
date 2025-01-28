#Импорт встроенной библиотеки
from datetime import datetime, date
#Цикл для карректного ввода данных с обработчиков ошибок
while True:
    user_input = input("Введите дату дедлайна заметки в формате дд.мм.гггг: ")
    try:
        user_date = datetime.strptime(user_input, "%d.%m.%Y").date()
        break
    except ValueError:
        print("Некорректный формат даты. Попробуйте еще раз.")

# Текущая дата
today = date.today()

# Разница между датами
delta = user_date - today

# Функция для проверки, что строка не пустая и содержит хотя бы 3 символа
def is_valid_input(input_str, min_length=3):
    return len(input_str.strip()) >= min_length

# Запрашиваем у пользователя информацию для создания заметки
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")



# Цикл на корректный ввод данных
valid_status = ["Активна","Выполнена","Отложена"]
while True:
    status = input("Введите статус заметки (например, 'Активна', 'Выполнена','Отложена'): ")

    if status in valid_status:
        break
    else:
        print("Неизвестный статус. Пожалуйста, выберите из: 'Активна','Выполнена','Отложена'")


# Проверка статуса
if status == "Активна":
    print("Заметка активна. Необходимо выполнить.")
elif status == "Выполнена":
    print("Заметка выполнена. Четко!")
elif status == "Отложено":
    print("Заметка отложена. Вернитесь к ней позже.")

# Создаем список для хранения заголовков заметки
titles = []

# Цикл для ввода заголовков заметки
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
#Блок кода для рассчета и предупреждения о дедлане для пользователя
if delta.days > 0:
    if delta.days <= 3:
        print(f"Внимание! Дедлайн через {delta.days} дней.")
    else:
        print(f"До дедлайна осталось {delta.days} дней.")
elif delta.days == 0:
    print("Срочно! Дедлайн сегодня!")
else:
    print(f"Дедлайн прошел {-delta.days} дней назад.")
print("Имя пользователя:", username)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Заголовки заметки:")
#Функция для корректного вывода списков заметок
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title}")