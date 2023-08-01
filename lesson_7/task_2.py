# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os

os.chdir("testdir")  # файлы будем переименовывать тут


def group_rename(name: str = 'NewNameFile', digits: int = 3, expansion: str = '', orig_name: list = [3, 6]):
    files = os.listdir(os.getcwd())
    for i in range(len(files)):
        extention = files[i].split('.')
        old_symbol = orig_symbol(files[i], orig_name)

        quantity_digits = add_digits(digits, i)

        if len(extention) > 1:
            if expansion == '':
                exp = extention[1]
            else:
                exp = expansion
            os.rename(files[i], f"{old_symbol}{name}{quantity_digits}.{exp}")


def orig_symbol(old_name: str, name: list[int, int]) -> str:
    first_symbol = name[0]
    end_symbol = name[1]
    rename = ''
    for i in range(first_symbol - 1, end_symbol - 1):
        rename += old_name[i]
    return rename


def add_digits(quantity: int, i: int) -> str:
    digits = ''
    count = 0
    while i > 0:
        a = i % 10
        digits += f"{a}"
        count += 1
        i = i // 10
    res = ''
    if quantity < count:
        res = "0" * (quantity - count)
    res += digits
    return res


if __name__ == '__main__':
    group_rename()
