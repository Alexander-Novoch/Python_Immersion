import logging
import argparse

logging.basicConfig(filename='task.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def triangle_check(a: float, b: float, c: float):
    triangle = f'Треугольник'
    result = ''
    if a + b < c or a + c < b or b + c < a:
        this_exception = f'Треугольник со сторонами {a}, {b}, {c} не может существовать'
        logger.error(this_exception)
        print(this_exception)
    else:
        if a == b == c:
            result = f' является равносторонним.'
        elif a == b or a == c or b == c:
            result = f' является равнобедренным.'
        else:
            result = f' является разносторонним.'

        logger.info(f'{triangle} со сторонами {a}, {b}, {c} - {result}')
        print(triangle + result)


def parse():
    parser = argparse.ArgumentParser(prog='triangle_check',
                                     description='проверка треугольника по заданым сторонам',
                                     epilog='triangle_check(5, 5, 5)')
    parser.add_argument('-a', '--A', default=5, help='Значение стороны a')
    parser.add_argument('-b', '--B', default=5, help='Значение стороны b')
    parser.add_argument('-c', '--C', default=5, help='Значение стороны c')
    args = parser.parse_args()
    return triangle_check(args.A, args.B, args.C)


if __name__ == '__main__':
    triangle_check(5, 5, 11)
    # parse()
