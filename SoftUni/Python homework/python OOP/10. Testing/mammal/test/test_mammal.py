from project.mammal import Mammal
from unittest import TestCase, main


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_mammal_init_create_all_attributes(self):
        self.assertEqual('name', self.mammal.name)
        self.assertEqual('mammal_type', self.mammal.type)
        self.assertEqual('sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = "name makes sound"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        expected_result = 'name is of type mammal_type'
        self.assertEqual(expected_result, self.mammal.info())


if __name__ == '__main__':
    main()