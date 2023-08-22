from Lesson_11.task_matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.matrix_3 = Matrix([[10, 2, 3], [40, 5, 6], [7, 8, 90]])
        self.matrix_4 = Matrix([[10, 2, 3], [40, 5, 6]])

    def test_create_matrix(self):
        self.assertEqual(self.matrix_4, Matrix([[10, 2, 3], [40, 5, 6]]))

    def test_equality_matrix(self):
        self.assertTrue(self.matrix_1 == self.matrix_2)

    def test_inequality_matrix(self):
        self.assertFalse(self.matrix_1 == self.matrix_3)

    def test_addition_matrix(self):
        self.assertEqual(self.matrix_1 + self.matrix_3, Matrix([[11, 4, 6], [44, 10, 12], [14, 16, 99]]))

    def test_multiplication_matrix(self):
        self.assertEqual(self.matrix_1 * self.matrix_3, Matrix([[111, 36, 285], [282, 81, 582], [453, 126, 879]]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
