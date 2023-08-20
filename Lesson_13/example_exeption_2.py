class DateExeption(Exception):
    def __init__(self, date: str):
        self.date = date

    def __str__(self):
        return f'Дата {self.date} не может существовать '


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    day, mon, year = map(int, str_date.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        raise DateExeption(str_date)

    if mon in (4, 6, 9, 11) and day > 30:
        raise DateExeption(str_date)

    if mon == 2 and if_leap(year) and day > 29:
        raise DateExeption(str_date)

    if mon == 2 and not if_leap(year) and day > 28:
        raise DateExeption(str_date)

    return True


if __name__ == '__main__':
    print(check_date('29.07.2023'))
