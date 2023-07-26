# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
# ___________________________________________________________________________
# Скрывать не буду, я позаимствовал код из 2го семинара, т.к. эту задачу я не делал
# Но я постарался максимально разбить его на функции, надеюсь у меня получилось)

user_info = {
    "money": 0,
    "oper_count": 0
}


def choise():
    menu_choise = input("""Пожалуйста, введите номер выбора, который вы хотите сделать   
             1 пополнить
             2 снять
             3 выйти
         Пожалуйста, введите ваш выбор :  """)
    return menu_choise


def bonus(user_oper_count):
    global user_money
    if user_oper_count > 3:
        user_money *= 1.03


def commission():
    global user_money
    withdrawl_persent = user_money - (user_money * 0.985)
    if withdrawl_persent < 30:
        withdrawl_persent = 30
    if withdrawl_persent > 600:
        withdrawl_persent = 600
    user_money = user_money - withdrawl_persent


def luxury_tax():
    global user_money
    if user_money > 5000000:
        user_money = user_money * 0.9


def introduction(value_str):
    try:
        value = int(value_str)
    except ValueError:
        print("Please, type a valid integer number!")
        return False
    if value < 1:
        print("Please type a strictly positive number!")
        return False
    elif value % 50 != 0:
        print("Please type a strictly кратны 50 у.е number!")
        return False
    else:
        return True


def extraction(value_str):
    try:
        value = int(value_str)
    except ValueError:
        print("Please, type a valid integer number!")
        return False
    if value < 1:
        print("Please type a strictly positive number!")
        return False
    elif value % 50 != 0:
        print("Please type a strictly кратны 50 у.е number!")
        return False
    elif value > user_money:
        print("Нельзя снять больше, чем на счёте!")
        return False
    else:
        return True


while True:

    user_money = user_info["money"]
    user_oper_count = user_info["oper_count"]
    match choise():
        case "1":
            luxury_tax()

            value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
            if introduction(value_str):
                user_money += int(value_str)

            bonus(user_oper_count)

            user_info["money"] = user_money
            user_info["oper_count"] = user_oper_count + 1
            print(user_money)
        case "2":
            luxury_tax()

            value_str = input("Сумма пополнения и снятия кратны 50 у.е : ")
            if extraction(value_str):
                user_money -= int(value_str)
                commission()
                bonus(user_oper_count)

            user_info["money"] = user_money
            user_info["oper_count"] = user_oper_count + 1
            print(user_money)
        case "3":
            print(user_money)
            break
