# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import pathlib

input_path: str = str(pathlib.Path(__file__))


def split_path(s: str):
    *a, b, c = s.replace('.', '\\').split('\\')
    new_a = '\\'.join(a)  # возвращаем первоначальный вид строке
    res = (new_a, b, c)
    return res


print(split_path(input_path))
