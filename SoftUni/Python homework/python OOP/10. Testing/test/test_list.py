from List.extended_list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.list_integers = IntegerList(4, 5, 6)

    def test_init_creates_all_attributes(self):
        self.assertEqual([4, 5, 6], self.list_integers._IntegerList__data)

    def test_init_takes_str_as_attribute(self):
        list_init = IntegerList('13', 3.2, 12.2)
        self.assertEqual([], list_init._IntegerList__data)

    def test_add_integer_element(self):
        result = self.list_integers.add(100)
        self.assertEqual([4, 5, 6, 100], result)

    def test_add_an_non_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.list_integers.add('111')

        expected_result = "Element is not Integer"
        self.assertEqual(expected_result, str(ve.exception))

    def test_remove_the_element_of_the_index(self):
        index = 1
        self.assertEqual([4, 5, 6], self.list_integers._IntegerList__data)
        el = self.list_integers.remove_index(index)
        self.assertEqual(5, el)
        self.assertEqual([4, 6], self.list_integers._IntegerList__data)

    def test_invalid_index(self):
        index = 4
        with self.assertRaises(IndexError) as ie:
            self.list_integers.remove_index(index)

        expected_result = "Index is out of range"
        self.assertEqual(expected_result, str(ie.exception))

    def test_get_specific_element(self):
        index = 1
        el = self.list_integers.get(index)
        self.assertEqual(5, el)

    def test_get_invalid_index(self):
        index = 4
        with self.assertRaises(IndexError) as ie:
            self.list_integers.get(index)

        expected_result = "Index is out of range"
        self.assertEqual(expected_result, str(ie.exception))

    def test_insert_adds_element_at_index(self):
        index, element = 1, 2
        self.assertEqual([4, 5, 6], self.list_integers._IntegerList__data)
        self.list_integers.insert(index, element)
        self.assertEqual([4, 2, 5, 6], self.list_integers._IntegerList__data)


    def test_insert_index_out_of_range(self):
        index, element = 4, 2

        with self.assertRaises(IndexError) as ie:
            self.list_integers.insert(index, element)

        expected_result = "Index is out of range"
        self.assertEqual(expected_result, str(ie.exception))

    def test_insert_element_is_not_integer(self):
        index, element = 1, '2'

        with self.assertRaises(ValueError) as ie:
            self.list_integers.insert(index, element)

        expected_result = "Element is not Integer"
        self.assertEqual(expected_result, str(ie.exception))

    def test_get_biggest(self):
        result = self.list_integers.get_biggest()
        self.assertEqual(6, result)

    def test_get_index(self):
        result = self.list_integers.get_index(5)
        self.assertEqual(1, result)


if __name__ == '__main__':
    main()