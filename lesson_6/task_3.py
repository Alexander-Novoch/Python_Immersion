# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
import task_2
import random

SIZE = 8
SUCCESSFUL_PLACEMENTS = 4


def random_qeens(size: int) -> list[tuple[int, int]]:  # почему-то выдаёт иногда 7 кортежей вместо 8??
    set_list = set()
    for i in range(size):
        set_list.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    list_point = list(set_list)
    return list_point


count = SUCCESSFUL_PLACEMENTS
while count >= 0:
    if task_2.chess(random_qeens(SIZE)):
        print(random_qeens(SIZE))
        print(task_2.chess(random_qeens(SIZE)))
    count -= 1

'''
В теории программа должна работать хоть и очень медленно (из-за большого количества случайных совпадений).
Но на практике, я заметил что список случайных значений почему-то не всегда коректно создаётся(
Пробовал переписывать, но безрезультатно(
'''

if __name__ == '__main__':
    print(random_qeens(SIZE))
    print(task_2.chess(random_qeens(SIZE)))
