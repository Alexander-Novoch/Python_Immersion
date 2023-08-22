import unittest
from Lesson_14.task_doctest import check_date


class TestCheckDate(unittest.TestCase):
    def test_true_date(self):
        self.assertTrue(check_date('29.07.2023'))

    def test_bad_date(self):
        self.assertFalse(check_date('31.06.2023'))

    def test_bad_month(self):
        self.assertFalse(check_date('29.13.2023'))

    def test_bad_leap(self):
        self.assertFalse(check_date('29.02.2023'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
