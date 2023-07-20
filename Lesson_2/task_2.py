# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


def get_number_from_user():
    fraction_number = input("Введите числитель и знаменатель дроби через пробел: ")
    numerator, denominator = fraction_number.split()
    return int(numerator), int(denominator)


number1, number2 = get_number_from_user()
number3, number4 = get_number_from_user()

common_denominator = number2 * number4
sum_of_fraction = (number1 * (common_denominator // number2)) + (number3 * (common_denominator // number4))
product_of_fractions = (number1*number3)
print(f"Сумма дробей: {sum_of_fraction}/{common_denominator}\n"
      f"Произведение дробей: {product_of_fractions}/{common_denominator}")


firstfraction = fractions.Fraction(number1, number2)
secondfraction = fractions.Fraction(number3, number4)
sum_fractions = firstfraction + secondfraction
product_fractions = firstfraction * secondfraction
print(f"Сумма дробей: {sum_fractions}\n"
      f"Произведение дробей: {product_fractions}")