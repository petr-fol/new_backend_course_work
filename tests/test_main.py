from src.main import main


def test_main():
    assert main() == """07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет 3861 14** **** **** 9794 -> Счет **8125
62814.53 руб.

30.10.2019 Перевод с карты на счет
Visa Gold 7756 67** **** 2839 -> Счет **9453
23036.03 руб.

29.09.2019 Перевод со счета на счет
Счет 3542 14** **** **** 9637 -> Счет **4961
45849.53 USD"""