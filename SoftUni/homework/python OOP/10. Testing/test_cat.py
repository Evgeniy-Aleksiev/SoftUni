from unittest import TestCase, main

class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
          raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
          raise Exception('Cannot sleep while hungry')

        self.sleepy = False


#from unittest import TestCase, main
class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Pesho')

    def test_cat_initialization(self):
        self.assertEqual('Pesho', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_cannot_eat_if_is_fed(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        expected_result = 'Already fed.'
        self.assertEqual(expected_result, str(ex.exception))

    def test_is_size_increased_after_eat(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertEqual(1, self.cat.size)

    def test_is_fed_after_eat(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_fall_asleep_if_not_fed(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        expected_result = 'Cannot sleep while hungry'
        self.assertEqual(expected_result, str(ex.exception))

    def test_fall_asleep(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
