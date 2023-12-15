import json
from check_functions import check_pattern

# ===========   Основные паттерны поиска  ==============================
#
#
namePattern = (r"^([А-ЯA-Z]|[А-ЯA-Z][\x27а-яa-z]{1,}|[А-ЯA-Z][\x27а-яa-z]{1,}\-([А-ЯA-Z][\x27а-яa-z]{1,}|" +
               "(оглы)|(кызы)))\040[А-ЯA-Z][\x27а-яa-z]{1,}(\040[А-ЯA-Z][\x27а-яa-z]{1,})?$")
phonePattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
BdayPattern = "%m/%d/%y"
emailPattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"


# ===========   Используемые функции  ==============================
#
#

def add(phonebook):
    fullname = check_pattern(1, namePattern, "Введите ФИО", False, 1)
    for key, el in phonebook.items():
        if key == fullname:
            print("Запись с таким именем уже имеется в справочнике !")
            print("Добавление данных отменено")
            return phonebook

    phones = check_pattern(1, phonePattern, "Введите номер телефона", True, 10)
    for key, el in phonebook.items():
        if len(set(el['phones']).intersection(phones)) > 0:
            print("Один из телофоных номеров уже имеется в справочникес !")
            print("Добавление данных отменено")
            return phonebook

    birthday = check_pattern(2, BdayPattern, "Введите дату рождения", True, 1)
    email = check_pattern(1, emailPattern, "Введите электронную почту", True, 1)
    for key, el in phonebook.items():
        if 'email' in el and el['email'] == email:
            print("Такой почтовый ящик уже существует в справочнике !")
            print("Добавление данных отменено")
            return phonebook

    phonebook[fullname] = {'phones': phones}
    if birthday != "":
        phonebook[fullname]['birthday'] = birthday
    if email != "":
        phonebook[fullname]['email'] = email
    print("Запись успешно добавлена!")

    return phonebook


def save(phonebook):
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    return phonebook


def show(phonebook):
    for key, values in phonebook.items():
        print(key, values)
    return phonebook


def search(phonebook):
    res_list = list()
    while True:
        print("    |-----------------------")
        print("    | Выберите поле поиска: ")
        print("    | 1 - По ФИО (часть имени)")
        print("    | 2 - По номеру телефона")
        search_field = input("    | Поле поиска: ").strip()
        print("    |-----------------------")
        match search_field:
            case "1":
                search_text = input("    | Введите ФИО либо его часть: ").strip()
                for key, value in phonebook.items():
                    if search_text in key:
                        res_list.append(key + ": " + str(value))
                break
            case "2":
                search_text = input("    | Введите номер телефона либо его часть: ").strip()
                for key, value in phonebook.items():
                    if 'phones' in value:
                        for el in value['phones']:
                            if search_text in el:
                                res_list.append(key + ": " + str(value))
                break
            case _:
                print("Выбрано неверное поле")

    if res_list:
        print("    | Результаты поиска:")
        for el in res_list:
            print(el)
    else:
        print("    | По заданным критериям ничего не найдено")

    return phonebook


def change(phonebook):
    res_list = list()
    print("    |-----------------------")
    search_text = input("    | Введите точное ФИО записи к внесению изменений: ").strip()
    print("    |-----------------------")
    search_key = ""
    for key, value in phonebook.items():
        if search_text in key:
            search_key = key
            res_list.append(key)
    if len(res_list) > 1:
        print("    | Найдено больше одной записи. Изменение не возможно.")
        return phonebook
    if not res_list:
        print("    | Запись к внесению изменений не найдена")
        return phonebook

    print("Вносятся изменения в следующую запись:")
    print(phonebook[search_key])
    print()
    phones = check_pattern(1, phonePattern, "Введите номер телефона", True, 10)
    for key, el in phonebook.items():
        if search_key != key and len(set(el['phones']).intersection(phones)) > 0:
            print("Один из телофоных номеров уже имеется в другой записи !")
            print("Изменение данных отменено")
            return phonebook

    birthday = check_pattern(2, BdayPattern, "Введите дату рождения", True, 1)
    email = check_pattern(1, emailPattern, "Введите электронную почту", True, 1)
    for key, el in phonebook.items():
        if search_key != key and 'email' in el and el['email'] == email:
            print("Такой почтовый ящик уже существует в другой записи !")
            print("Изменение данных отменено")
            return phonebook

    phonebook[search_key] = {'phones': phones}
    if birthday != "":
        phonebook[search_key]['birthday'] = birthday
    if email != "":
        phonebook[search_key]['email'] = email

    return phonebook


def delete(phonebook):
    res_list = list()
    print("    |-----------------------")
    search_text = input("    | Введите точное ФИО записи для удаления: ").strip()
    print("    |-----------------------")
    search_key = ""
    for key, value in phonebook.items():
        if search_text in key:
            search_key = key
            res_list.append(key)
    if len(res_list) > 1:
        print("    | Найдено больше одной записи. Удаление не возможно.")
        return phonebook
    if not res_list:
        print("    | Запись для удаления не найдена")
        return phonebook

    print("Удаляется следующая запись:")
    print(search_key + ": " + phonebook.pop(search_key))
    print()

    return phonebook

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
