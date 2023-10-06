import json


def get_json_file():
    """ Загружаем файл с банковскими операциями. """

    with open('operations.json', "r", encoding="utf-8") as file:
        file_ = json.load(file)
    return file_


def sort_ex(json_file):
    """ Отсекаем не EXECUTED операции. """
    ex_list = []
    for operation in json_file:
        if "state" in operation:  # убрал блок (and "from" in operation)
            if operation["state"] == "EXECUTED":
                ex_list.append(operation)
    return ex_list


def get_date(date_str, mode):
    """ берет строку date и возращает дату/вермя/значение даты"""
    date = date_str.split('T')[0]
    time = date_str.split('T')[1]
    date_list = date.split('-')
    time_list = time.split(':')
    time_list = [int(float(i)) for i in time_list]

    if mode == 'date':
        return date_list
    elif mode == 'time':
        return time_list
    elif mode == 'value':
        date_list = [int(i) for i in date_list] + time_list
        value = (date_list[0] * 365 + date_list[1] * 365 / 12 + date_list[2] +
                 date_list[3] / 24 + date_list[4] / 24 / 60 + date_list[5] / 24 / 60 / 60)
        return value


def sort_date(json_file_ex):
    """ Сортирует список операций по дате. """
    sorted_list = sorted(json_file_ex, key=lambda operation: get_date(operation["date"], "value"), reverse=True)
    return sorted_list[:5]


def mask_operation(operation_ex):
    """ Маскирует номер карт перевода звездочками. """
    from_ = operation_ex.get("from")  # заменил получение значения из from, так как сейчас оно может отсутствовать.
    # Если мы получаем через get значение и его нет в словаре, то запишется None
    to = operation_ex["to"]
    desc_from_ = ""
    desc_to = ""
    num_from_str = ""
    num_to_str = ""

    if from_:  # добавил блок, что если from_ не является None, то делаем действия, иначе оставляем пустой строкой
        for symbol in from_:
            if symbol.isdigit():
                num_from_str += symbol
            else:
                desc_from_ += symbol
    for symbol in to:
        if symbol.isdigit():
            num_to_str += symbol
        else:
            desc_to += symbol

    if len(num_from_str) == 16:
        num_from_str = num_from_str.replace(num_from_str[6:12], "******")
        num_from_list = [num_from_str[0:4], num_from_str[4:8], num_from_str[8:12], num_from_str[12:]]
    elif len(num_from_str) == 20:
        num_from_str = num_from_str.replace(num_from_str[6:16], "**********")
        num_from_list = [num_from_str[0:4], num_from_str[4:8], num_from_str[8:12],
                         num_from_str[12:16], num_from_str[16:20]]
    else:
        num_from_list = []  # Так как num_from_str может быть пустой строкой, то создадим список num_from_list пустым.

    if len(num_to_str) == 16:
        num_to_str = num_to_str.replace(num_to_str[:12], "************")
        num_to_list = [num_to_str[10:12], num_to_str[12:16]]
    elif len(num_to_str) == 20:
        num_to_str = num_to_str.replace(num_to_str[:16], "****************")
        num_to_list = [num_to_str[14:16], num_to_str[16:20]]
    return [desc_from_, " ".join(num_from_list), desc_to, "".join(num_to_list)]


def for_print(operation):
    """ Печатает операцию в виде строки. """
    date_list = get_date(operation["date"], "date")
    date = '.'.join(reversed([str(i) for i in date_list]))
    desc = operation["description"]
    masked_list = mask_operation(operation)
    amount = operation["operationAmount"]["amount"]
    name = operation["operationAmount"]["currency"]["name"]
    return (f"{date} {desc}\n"
            f"{masked_list[0]}{masked_list[1]} -> {masked_list[2]}{masked_list[3]}\n"
            f"{amount} {name}\n")
