from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTest(TestCase):
    STUDENT_NAME = 'Pesho'
    SUBJECT_MATH = 'Mathematics'
    SUBJECT_HISTORY = 'History'
    SCHOOL_YEAR = 4

    def setUp(self) -> None:
        self.student = StudentReportCard('Pesho', 4)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.STUDENT_NAME, self.student.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_invalid_name_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            student = StudentReportCard('', 4)

        expected_result = 'Student Name cannot be an empty string!'
        self.assertEqual(expected_result, str(ve.exception))

    def test_student_name_property_with_valid_name_should_return_value(self):
        new_name = "Gosho"
        self.student.student_name = new_name
        self.assertEqual(new_name, self.student.student_name)

    def test_invalid_school_year_lower_number(self):
        with self.assertRaises(ValueError) as ve:
            student = StudentReportCard(self.STUDENT_NAME, 0)

        expected_result = "School Year must be between 1 and 12!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_invalid_school_year_bigger_number(self):
        with self.assertRaises(ValueError) as ve:
            student = StudentReportCard(self.STUDENT_NAME, 13)

        expected_result = "School Year must be between 1 and 12!"
        self.assertEqual(expected_result, str(ve.exception))

    def test_add_grade_subject_not_in_grades_by_subject(self):
        self.assertFalse(self.SUBJECT_MATH in self.student.grades_by_subject)
        self.student.add_grade(self.SUBJECT_MATH, 4)
        expected_result = {self.SUBJECT_MATH: []}
        expected_result[self.SUBJECT_MATH].append(self.SCHOOL_YEAR)
        self.assertEqual(expected_result, self.student.grades_by_subject)

    def test_add_grade(self):
        self.student.add_grade(self.SUBJECT_MATH, 4)
        self.assertTrue(self.SUBJECT_MATH in self.student.grades_by_subject)
        self.student.add_grade(self.SUBJECT_MATH, 4)

        expected_result = {self.SUBJECT_MATH: [4, 4]}
        self.assertEqual(expected_result, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.add_grade(self.SUBJECT_MATH, 4)
        self.student.add_grade(self.SUBJECT_MATH, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)

        result = self.student.average_grade_by_subject()
        expected_result = ''

        for subject, grade in self.student.grades_by_subject.items():
            expected_result += f'{subject}: {(sum(grade) / len(grade)):.2f}\n'

        self.assertEqual(expected_result.strip(), result)

    def test_average_grade_for_all_subjects(self):
        grade_1, grade_2, grade_3, grade_4 = 4, 5, 5, 5

        self.student.add_grade(self.SUBJECT_MATH, 4)
        self.student.add_grade(self.SUBJECT_MATH, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)

        average_grade = (grade_1 + grade_2 + grade_3 + grade_4) / 4

        result = self.student.average_grade_for_all_subjects()
        expected_result = f"Average Grade: {average_grade:.2f}"
        self.assertEqual(expected_result, result)

    def test_repr(self):
        self.student.add_grade(self.SUBJECT_MATH, 4)
        self.student.add_grade(self.SUBJECT_MATH, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)
        self.student.add_grade(self.SUBJECT_HISTORY, 5)

        expected_report = f"Name: {self.STUDENT_NAME}\n" \
                 f"Year: {self.SCHOOL_YEAR}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_for_all_subjects()}"

        result = repr(self.student)
        self.assertEqual(expected_report, result)


if __name__ == '__main__':
    main()
