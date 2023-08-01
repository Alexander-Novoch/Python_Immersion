# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона
# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
from string import ascii_lowercase, digits
from random import choices, randint
from os import path


def check_dir(dir, **kwargs) -> None:
    if not path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    many_extensions(**kwargs)


def make_files(ext: str, max_name_len: int = 30, min_name_len: int = 6,
               min_byte_len: int = 256, max_byte_len: int = 4096, quantity: int = 42) -> None:
    for i in range(quantity):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name_len, max_name_len)))
        byte_array = bytes(randint(0, 255))
        for _ in range(randint(min_byte_len, max_byte_len)):
            with open(rf'{name}.{ext}', 'wb') as many_files:
                many_files.write(byte_array)


def many_extensions(**kwargs):
    for ext, quantity in kwargs.items():
        make_files(ext, quantity=quantity)


if __name__ == '__main__':
    check_dir(r'.\\testdir', gif=9, doc=12, txt=4)
