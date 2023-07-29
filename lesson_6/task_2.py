# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

SIZE = 8

queens = [(3, 0), (0, 1), (4, 2), (7, 3), (1, 4), (6, 5), (2, 6), (5, 7)]


def chess(points: list) -> bool:
    check = True
    x = []
    y = []
    for i in range(SIZE):  # x, y = list(map(list, zip(*points)))
        x.append(points[i][0])
        y.append(points[i][1])

    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                check = False
    return check


def print_chess(points: list):
    for i in range(len(points)):
        print('')
        for j in range(len(points)):
            if points[i][0] == j and points[i][1] == i:
                print(f'{i + 1}\t', end='')
            else:
                print('*\t', end='')


if __name__ == '__main__':
    print(chess(queens))
    print_chess(queens)
