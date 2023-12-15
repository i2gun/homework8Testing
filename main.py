# Урок 8. Работа с файлами
# Основной функционал - просмотр, сохранение, добавление (импорт), поиск, удаление, изменениею

import json
from command_functions import add, save, show, search, change, delete

loopGoOn = True
phonebook = {"Дядя Ваня": {'phones': ['84951116565', '89651115544'], 'birthday': "05.05.1990", 'email': "12@ya.ru"},
             "Дядя Вася": {'phones': ['84994445151']}}
try:
    with open("contacts.json", "r", encoding="utf-8") as fh:
        phonebook = json.loads(fh.read())
except Exception:
    print("Загрузка тестового телефонного справочника")


def finish(record):
    global loopGoOn
    loopGoOn = False
    return record


commands = {"add": add, "save": save, "show": show, "find": search,
            "change": change, "del": delete, "quit": finish, "exit": finish}
while loopGoOn:
    print("    |-----------------------")
    print("    |  Вам доступны следующие команды: add, save, show, find, change, del, quit")
    command = input("    |  Введите новую команду: ").strip()
    print("    |-----------------------")
    try:
        phonebook = commands[command](phonebook)
    except Exception:
        print("Неверная комманда")