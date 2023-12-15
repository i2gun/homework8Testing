import command_fucntions

loopGoOn = True
phonebook = command_fucntions.load()
commands = {"add": command_fucntions.add, "save": command_fucntions.save,
            "show": command_fucntions.show, "search": command_fucntions.search,
            "change": command_fucntions.change, "del": command_fucntions.delete
            }
while loopGoOn:
    print("-----------------------")
    print("Вам доступны следующие команды: add, save, show, search, change, del, quit")
    if command := input("Введите новую команду: ") == "quit":
        break
    print("-----------------------")
    try:
        phonebook = commands[command](phonebook)
    except:
        print("Неверная комманда")

# Урок 8. Работа с файлами
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
#
# Формат сдачи: ссылка на свой репозиторий в гитхаб.
