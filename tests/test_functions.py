from src.functions import *


def test_sort_ex():
    operations = [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 441945886,
            "state": "CANCELED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
    ]
    executed_operations = sort_ex(operations)

    assert len(executed_operations) == 1
    assert executed_operations[0].get('state') == 'EXECUTED'


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
    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
    ]
    operations = sort_date(operations)
    assert len(operations) == 2
    assert operations[0].get('date') == '2019-12-08T22:46:21.935582'
    assert operations[1].get('date') < operations[0].get('date')


def test_mask_operations():
    operations = [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
    ]
    masked1 = mask_operation(operations[0])
    masked2 = mask_operation(operations[1])
    assert masked1 == ['', '', 'Счет ', '**5907']
    assert masked2 == ['Maestro ', '1596 83** **** 5199', 'Счет ', '**9589']
