import pytest
from Lesson_14.task_doctest import check_date


def test_true_date():
    assert check_date('29.07.2023') == True


def test_bad_date():
    assert check_date('31.06.2023') == False


def test_bad_month():
    assert check_date('29.13.2023') == False


def test_bad_leap():
    assert check_date('29.02.2023') == False


if __name__ == '__main__':
    pytest.main(['-vv'])
