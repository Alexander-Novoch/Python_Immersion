# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.
SIZE = 8
queens = [(3, 0), (0, 1), (4, 2), (7, 3), (1, 4), (6, 5), (2, 6), (5, 7)]


class EightQueens:
    def __init__(self, possible_option: list, size: int = 8):
        self.points = possible_option
        self.size = size

    def check_queens(self) -> bool:
        check = True
        x = []
        y = []
        for i in range(int(self.size)):  # x, y = list(map(list, zip(*points)))
            x.append(self.points[i][0])
            y.append(self.points[i][1])

        for i in range(self.size):
            for j in range(i + 1, self.size):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    check = False
        return check

    def print_chess(self):
        for i in range(len(self.points)):
            print('')
            for j in range(len(self.points)):
                if self.points[i][0] == j and self.points[i][1] == i:
                    print(f'{i + 1}\t', end='')
                else:
                    print('*\t', end='')


if __name__ == '__main__':
    option = EightQueens(queens, SIZE).check_queens()
    print(option)
    option = EightQueens(queens, SIZE).print_chess()
