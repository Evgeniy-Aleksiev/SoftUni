import unittest


class SimpleTest(unittest.TestCase):
    def test_upper(self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
