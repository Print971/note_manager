#Создаем пустой список
new_titi = []
#Создаем цикл для постоянного сбора данных с условиями
while True:
    user_name = input("Введите имя: ")
    content = input("Введите заголовок заметки: ")
    titels = input("Введите описание заметки: ")
    status = input("Введите статус заметки: ")
    new_data = input("Дата создания заметки: ")
    dead_line = input("Дедлайн заметки: ")

    user_titel = {
        "Имя": user_name,
        "Заголовок": content,
        "Описание": titels,
        "Статус": status,
        "Дата создания": new_data,
        "Дедлайн": dead_line
    }
#Этой командой мы поместили словарь внутрь списка
    new_titi.append(user_titel)

  # Спрашиваем пользователя, хочет ли он создать еще одну заметку
    titel = input("Создать еще одну заметку? (Да/Нет): ")
    if titel.lower() != "да":  # Преобразуем ввод в нижний регистр для удобства
        break  # Выход из цикла, если пользователь ввел что-то кроме "да"


#Выводим все значения от пользователя на экран
print("Список заметок:")
for user in new_titi:
    print(user)












