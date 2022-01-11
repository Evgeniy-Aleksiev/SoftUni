from project.train.train import Train
from unittest import TestCase, main


class TrainTest(TestCase):
    PASSENGER = 'Goshka'

    def setUp(self) -> None:
        self.train = Train('Loko', 100)

    def test_init_creates_all_attributes(self):
        self.assertEqual('Loko', self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_raise_exception_train_is_full(self):
        train = Train('Loko', 0)
        self.assertTrue(train.capacity == len(train.passengers))

        with self.assertRaises(ValueError) as ve:
            train.add(self.PASSENGER)

        self.assertEqual("Train is full", str(ve.exception))

    def test_add_passenger_raise_exception_passenger_exists(self):
        self.train.add(self.PASSENGER)
        self.assertTrue(self.PASSENGER in self.train.passengers)

        with self.assertRaises(ValueError) as ve:
            self.train.add(self.PASSENGER)

        self.assertEqual(f'Passenger {self.PASSENGER} Exists', str(ve.exception))

    def test_add_successfully_passenger_to_train(self):
        result = self.train.add(self.PASSENGER)
        self.assertTrue(self.PASSENGER in self.train.passengers)
        self.assertEqual(f'Added passenger {self.PASSENGER}', result)

    def test_remove_passenger_raise_exception_passenger_not_exists(self):
        self.assertFalse(self.PASSENGER in self.train.passengers)

        with self.assertRaises(ValueError) as ve:
            self.train.remove(self.PASSENGER)

        self.assertEqual(f'Passenger Not Found', str(ve.exception))

    def test_successfully_remove_passenger_from_train(self):
        self.train.add(self.PASSENGER)
        self.assertTrue(self.PASSENGER in self.train.passengers)
        result = self.train.remove(self.PASSENGER)
        self.assertFalse(self.PASSENGER in self.train.passengers)
        self.assertEqual(f'Removed {self.PASSENGER}', result)


if __name__ == '__main__':
    main()