import json
from check_functions import check_pattern


def add(phonebook):
    pattern = (r"^([А-ЯA-Z]|[А-ЯA-Z][\x27а-яa-z]{1,}|[А-ЯA-Z][\x27а-яa-z]{1,}\-([А-ЯA-Z][\x27а-яa-z]{1,}|" +
               "(оглы)|(кызы)))\040[А-ЯA-Z][\x27а-яa-z]{1,}(\040[А-ЯA-Z][\x27а-яa-z]{1,})?$")
    fullname = check_pattern(1, pattern, "Введите ФИО", False, 1)

    pattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    phones = check_pattern(1, pattern, "Введите номер телефона", True, 10)

    pattern = "%m/%d/%y"
    birthday = check_pattern(2, pattern, "Введите дату родения", True, 1)

    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    email = check_pattern(1, pattern, "Введите электронную почту", True, 1)

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
    print("Выберите поле поиска: ")
    print("1 - По ФИО (часть имени)")
    print("2 - По номеру телефона")
    for key, values in phonebook.items():
        print(key, values)


def change(phonebook):
    for key, values in phonebook.items():
        print(key, values)


def delete(phonebook):
    for key, values in phonebook.items():
        print(key, values)

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных