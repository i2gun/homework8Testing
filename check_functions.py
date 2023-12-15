import re
import datetime


def check_date(pattern, text):
    try:
        datetime.datetime.strptime(text, pattern)
    except Exception:
        return False
    return True


def check_func(check_type, pattern, text):
    if check_type == 1:
        return re.fullmatch(re.compile(pattern), text)
    elif check_type == 2:
        return check_date(pattern, text)


def check_pattern(check_type, pattern, msg, check_for_quit, item_num):
    out = list() if item_num > 1 else ""
    first_mandatory = check_for_quit and item_num > 1     # first phone number is mandatory
    while item_num > 0:
        if first_mandatory:
            text = input(msg + " (хотя бы один номер обязателен): ").strip()
        else:
            text = input(msg + (", либо 'q' для выхода: " if check_for_quit else ": ")).strip()
        if check_func(check_type, pattern, text):
            if type(out) is list:
                out.append(text)
            else:
                out = text
            item_num -= 1
            first_mandatory = False
        else:
            if check_for_quit and not first_mandatory and text == "q":
                break
            else:
                print("Введено неверное значение")

    return out