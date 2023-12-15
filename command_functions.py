import json
from check_functions import check_pattern

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
    phones = check_pattern(1, phonePattern, "Введите номер телефона", True, 10)
    birthday = check_pattern(2, BdayPattern, "Введите дату рождения", True, 1)
    email = check_pattern(1, emailPattern, "Введите электронную почту", True, 1)

    phonebook[fullname] = {'phones': phones}
    if birthday != "":
        phonebook[fullname]['birthday'] = birthday
    if email != "":
        phonebook[fullname]['email'] = email


def save(phonebook):
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))


def show(phonebook):
    for key, values in phonebook.items():
        print(key, values)


def search(phonebook):
    res_list = list()
    while True:
        print("    |-----------------------")
        print("    | Выберите поле поиска: ")
        print("    | 1 - По ФИО (часть имени)")
        print("    | 2 - По номеру телефона")
        search_field = input("    | Поле поиска: ")
        print("    |-----------------------")
        match search_field:
            case "1":
                search_text = input("    | Введите ФИО либо его часть: ")
                for key, value in phonebook:
                    if search_text in key:
                        res_list.append(key)
                break
            case "2":
                search_text = input("    | Введите номер телефона либо его часть: ")
                for key, value in phonebook:
                    for el in value.items():
                        if search_text in el:
                            res_list.append(el)
                break
            case _:
                print("Выбрано неверное поле")

    return res_list


def change(phonebook):
    for key, values in phonebook.items():
        print(key, values)


def delete(phonebook):
    for key, values in phonebook.items():
        print(key, values)

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
