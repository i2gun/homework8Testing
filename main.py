import json
from command_functions import add, save, show, search, change, delete

loopGoOn = True


def finish():
    global loopGoOn
    loopGoOn = False


phonebook = {"Дядя Ваня": {'phones': [8311654654, 89654515], 'birthday': "05.05.1990", 'email': "12@ya.ru"},
             "Дядя Вася": {'phones': [54654541]}}
try:
    with open("contacts.json", "r", encoding="utf-8") as fh:
        phonebook = json.loads(fh.read())
except:
    print("Загрузка тестового телефонного справочника")

commands = {"add": add, "save": save,
            "show": show, "find": search,
            "change": change, "del": delete,
            "quit": finish, "exit": finish}
while loopGoOn:
    print("    |-----------------------")
    print("    |  Вам доступны следующие команды: ", commands.keys())
    command = input("    |  Введите новую команду: ")
    print("    |-----------------------")
    try:
        phonebook = commands[command](phonebook)
    except Exception:
        print("Неверная комманда")

# Урок 8. Работа с файлами
# основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
#
# Формат сдачи: ссылка на свой репозиторий в гитхаб.
