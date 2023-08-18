# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
import csv
from itertools import chain


class Validate:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    @staticmethod
    def validate(value):
        if not isinstance(value, str):
            raise TypeError(f'Значение {value} должно быть текстом')
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    first_name = Validate()
    patronymic = Validate()
    last_name = Validate()

    def __init__(self, first_name, patronymic, last_name):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.subject_grades = {}
        self.subject_tests = {}

        with open('educational_journal.csv', 'r', encoding='utf-8') as csv_file:
            subjects = csv.reader(csv_file, delimiter="\n")
            for item in subjects:
                self.subject_grades[item[0]] = []
                self.subject_tests[item[0]] = []

    def add_score(self, score, subject):
        if score < 2 or score > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subject_grades[subject].append(score)

    def add_test_result(self, result, subject):
        if result < 0 or result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subject_tests[subject].append(result)

    def average_score_student(self):
        subject_scores = [sum(score) for score in self.subject_grades.values() if score != []]
        divider = [1 for item in self.subject_grades.values() for i in item]
        if not subject_scores:
            return 0
        return sum(subject_scores) / sum(divider)

    def subject_test_average(self, subject):
        return subject, sum(self.subject_tests[subject]) / len(self.subject_tests[subject])

    def __repr__(self):
        return f'Student({self.first_name} , {self.patronymic} , {self.last_name})'


if __name__ == '__main__':
    student = Student('Иван', "Иванович", "Иванов")
    print(student)

    # Добавление оценок и результатов тестов
    student.add_score(4, 'Math')
    student.add_score(4, 'Math')
    student.add_score(4, 'Russian')
    student.add_score(5, 'Russian')
    student.add_score(3, 'Physics')
    student.add_score(4, 'Physics')
    student.add_score(4, 'Physics')

    student.add_test_result(80, 'Math')
    student.add_test_result(90, 'Russian')
    student.add_test_result(20, 'Russian')

    # Расчёт среднего балла ученика по всем предметам
    print("Средний балл ученика", student.average_score_student())

    # Расчёт среднего балла по тестам определенного предмета
    print("Средний балл по тесту:", student.subject_test_average('Russian'))
