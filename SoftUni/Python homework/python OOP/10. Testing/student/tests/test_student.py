from project.student import Student
from unittest import TestCase, main

class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('Gosho', {'Python': ['n1', 'n2']})

    def test_student_init_create_all_attributes(self):
        for course in [{'Python': ['n1', 'n2']}, None]:
            self.student = Student('Gosho', course)
            if course is None:
                course = {}

            self.assertEqual('Gosho', self.student.name)
            self.assertEqual(course, self.student.courses)

    def test_enroll_course_name_in_course_keys(self):
        result = self.student.enroll('Python', ['n3'], '')
        expected_result = "Course already added. Notes have been updated."

        self.assertEqual(expected_result, result)
        self.assertEqual(['n1', 'n2', 'n3'], self.student.courses['Python'])

    def test_enroll_add_course_notes_and_courses(self):
        for idx, command in enumerate(['Y', '']):
            courses_name = f'C#{idx}'
            courses_notes = ['n3', 'n4']
            result = self.student.enroll(courses_name, courses_notes, command)

            expected_result = "Course and course notes have been added."
            self.assertEqual(expected_result, result)
            self.assertTrue(courses_name in self.student.courses)
            self.assertEqual(courses_notes, self.student.courses[courses_name])

    def test_add_course(self):
        courses_name = f'C#'
        result = self.student.enroll(courses_name, ['OOP', 'Inheritance'], 'Z')
        expected_result = "Course has been added."

        self.assertEqual(expected_result, result)
        self.assertTrue(courses_name in self.student.courses)
        self.assertEqual([], self.student.courses[courses_name])

    def test_add_notes(self):
        result = self.student.add_notes('Python', 'n3')
        expected_result = "Notes have been updated"

        self.assertEqual(expected_result, result)
        self.assertEqual(['n1', 'n2', 'n3'], self.student.courses['Python'])

    def test_add_notes_should_raise_an_error(self):
        course_name = 'C#'

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name, ['n3', 'n4'])

        expected_result = "Cannot add notes. Course not found."
        self.assertEqual(expected_result, str(ex.exception))

    def test_leave_course(self):
        course_name = 'Python'
        self.student.leave_course(course_name)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_should_raise_an_error(self):
        course_name = 'C#'
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course_name)

        self.assertEqual(expected_result, str(ex.exception))


if __name__ == '__main__':
    main()