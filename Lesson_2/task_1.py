# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

HEX_DEVIDER = 16
HEX_SIMBOL = "0123456789ABCDEF"
hex_number = ""


def get_number_from_user():
    d = input("Введите число: ")
    return int(d)


decimal_number = get_number_from_user()

print(f"Шестнадцатеричное число встроенной функции  -  {hex(decimal_number)}")

while decimal_number > 0:
    r = decimal_number % 16
    hex_digit = HEX_SIMBOL[r]
    hex_number = hex_digit + hex_number
    decimal_number //= 16

print(f"Шестнадцатеричное число нашей функции  -  {hex_number}")