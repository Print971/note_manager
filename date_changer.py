# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
day,month,_= created_date.split(".")
formatted_date = f"{day}.{month}."

issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
day,month,_= issue_date.split(".")
formatted_date1 = f"{day}.{month}."


# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:",formatted_date)
print("Дата истечения заметки:",formatted_date1)
