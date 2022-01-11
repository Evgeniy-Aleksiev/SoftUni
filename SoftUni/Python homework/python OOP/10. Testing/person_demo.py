import unittest


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Evgeniy', 'Aleksiev', 23)

    def test_get_full_name(self):
        result = self.person.get_full_name()
        expected_result = 'Evgeniy Aleksiev'
        self.assertEqual(expected_result, result)

    def test_get_person_info(self):
        result = self.person.get_info()
        expected_result = 'Evgeniy Aleksiev is 23 years old'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()

