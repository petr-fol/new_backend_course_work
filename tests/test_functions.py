from src.functions import *


# def test_get_json_file():
#     f = get_json_file()
#     assert f is not None
#     assert isinstance(f, list)
#     assert all(isinstance(elem, dict) for elem in f)
#
#     # # Дополнительные проверки
#     # assert len(f) > 0  # Проверяем, что список не пустой
#     # assert all("state" is not None)  # Проверяем, что в каждом элементе есть ключ "state"
#     # assert all("date" is not None)  # Проверяем, что в каждом элементе есть ключ "date"
#     # assert all("description" is not None)  # Проверяем, что в каждом элементе есть ключ "description"
#     # assert all("operationAmount" is not None)  # Проверяем, что в каждом элементе есть ключ "operationAmount"
#     # assert all(elem["state"] is not None for elem in f)  # Проверяем, что значение ключа "state" не является пустым
#     # assert all(elem["date"] is not None for elem in f)  # Проверяем, что значение ключа "date" не является пустым
#     # assert all(elem["description"] is not None for elem in f)  # Проверяем, что значение ключа "description" не является пустым
#     # assert all(elem["operationAmount"] is not None for elem in f)  # Проверяем, что значение ключа "operationAmount" не является пустым
#

def test_sort_ex():
    json_file = get_json_file()
    executed_operations = sort_ex(json_file)

    assert isinstance(executed_operations, list)
    assert all(isinstance(operation, dict) for operation in executed_operations)
    assert all(operation["state"] == "EXECUTED" for operation in executed_operations)
    assert all("description" in operation for operation in executed_operations)
    assert all("operationAmount" in operation for operation in executed_operations)

    # Дополнительные проверки
    assert all("date" in operation for operation in executed_operations)  # Проверяем, что в каждом элементе есть ключ "date"
    assert all("from" in operation for operation in executed_operations)  # Проверяем, что в каждом элементе есть ключ "from"
    assert all("to" in operation for operation in executed_operations)  # Проверяем, что в каждом элементе есть ключ "to"
    assert all(operation["date"] is not None for operation in executed_operations)  # Проверяем, что значение ключа "date" не является пустым
    assert all(operation["from"] is not None for operation in executed_operations)  # Проверяем, что значение ключа "from" не является пустым
    assert all(operation["to"] is not None for operation in executed_operations)  # Проверяем, что значение ключа "to" не является пустым


def test_get_date():
    date = get_date("2020-01-01T00:0:2", "date")
    time = get_date("2020-01-01T00:0:2", "time")
    value_date = get_date("2020-01-01T00:0:2", "value")

    assert isinstance(date, list)
    assert len(date) == 3
    assert all(isinstance(elem, str) for elem in date)

    assert isinstance(time, list)
    assert len(time) == 3
    assert all(isinstance(elem, int) for elem in time)

    assert isinstance(value_date, float)
    assert value_date == 737331.4166898148


def test_sort_date():
    f = sort_date(sort_ex(get_json_file()))
    assert len(f) == 5
    assert isinstance(f, list)
    assert all(isinstance(elem, dict) for elem in f)
    assert all("state" in elem for elem in f)
    assert all("date" in elem for elem in f)
    assert all("description" in elem for elem in f)
    assert all("operationAmount" in elem for elem in f)
    assert all("from" in elem for elem in f)
    assert all("to" in elem for elem in f)
    assert all(elem["state"] is not None for elem in f)  # Проверяем, что значение ключа "state" не является пустым
    assert all(elem["date"] is not None for elem in f)  # Проверяем, что значение ключа "date" не является пустым
    assert all(elem["description"] is not None for elem in f)  # Проверяем, что значение ключа "description" не является пустым
    assert all(elem["operationAmount"] is not None for elem in f)  # Проверяем, что значение ключа "operationAmount" не является пустым
    assert all(elem["from"] is not None for elem in f)  # Проверяем, что значение ключа "from" не является пустым
    assert all(elem["to"] is not None for elem in f)  # Проверяем, что значение ключа "to" не является пустым


def test_mask_operations():
    operations = sort_ex(get_json_file())
    masked = mask_operation(operations[0])
    assert len(masked) == 4
    assert isinstance(masked, list)
    assert all(isinstance(elem, str) for elem in masked)
    assert all(len(elem) > 0 for elem in masked)  # Проверяем, что все строки в списке `masked` не пустые


def test_for_print():
    operation = {
        "id": 114832369,
        "state": "EXECUTED",
        "date": "2019-12-07T06:17:14.634890",
        "operationAmount": {
            "amount": "48150.39",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655"
    }
    result = for_print(operation)
    assert isinstance(result, str)

    expected_result = ("07.12.2019 Перевод организации\n"
                       "Visa Classic 2842 87** **** 9012 -> Счет **3655\n"
                       "48150.39 USD\n")
    assert result == expected_result