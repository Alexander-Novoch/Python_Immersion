# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MAX_LIMIT = 100000
SIMPLE = 2
COMPOSITE = 1
a = int(input("Введите число от 1 до 100000: "))

x = 0
if a <= 0 or a > MAX_LIMIT:
    print("Введите другое число")
else:
    for i in range(2, a):
        if a % i == 0:
            x = COMPOSITE
            break
        else:
            x = SIMPLE

if x == COMPOSITE:
    print("Это составное число")
elif x == SIMPLE:
    print("Это простое число")