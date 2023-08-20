class TriangleExseption(Exception):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не может существовать'


def triangle_check(a: float, b: float, c: float):
    if a + b < c or a + c < b or b + c < a:
        raise TriangleExseption(a, b, c)
    else:
        if a == b == c:
            print("Треугольник является равносторонним.")
        elif a == b or a == c or b == c:
            print("Треугольник является равнобедренным.")
        else:
            print("Треугольник является разносторонним.")


if __name__ == '__main__':
    triangle_check(5, 5, 11)
