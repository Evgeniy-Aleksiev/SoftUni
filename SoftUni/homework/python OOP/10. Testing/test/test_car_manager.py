from CarManager.car_manager import Car
from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self) -> None:
        self.car = Car(make='Test', model='TestModel', fuel_consumption=5.6, fuel_capacity=75)

    def test_car_init_create_all_attributes(self):
        self.assertEqual('Test', self.car.make)
        self.assertEqual('TestModel', self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_setter_invalid_make_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        expected_result = "Make cannot be null or empty!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_setter_invalid_make_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = 0

        expected_result = "Make cannot be null or empty!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_setter_invalid_model_empty(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        expected_result = "Model cannot be null or empty!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_setter_invalid_model_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = 0

        expected_result = "Model cannot be null or empty!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        expected_result = "Fuel consumption cannot be zero or negative!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_consumption(self):
        self.car.fuel_consumption = 1
        self.assertEqual(1, self.car.fuel_consumption)

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        expected_result = "Fuel capacity cannot be zero or negative!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_capacity(self):
        self.car.fuel_capacity = 1
        self.assertEqual(1, self.car.fuel_capacity)

    def test_fuel_amount_cannot_be_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        expected_result = "Fuel amount cannot be negative!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_fuel_amount(self):
        self.car.fuel_amount = 1
        self.assertEqual(1, self.car.fuel_amount)

    def test_fuel_cannot_be_null_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        expected_result = "Fuel amount cannot be zero or negative!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_refuel_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(25)
        self.assertEqual(25, self.car.fuel_amount)

    def test_drive_dont_have_enough_fuel(self):
        self.car.refuel(25)  # fuel_amount = 25

        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        expected_result = "You don't have enough fuel to drive!"
        self.assertEqual(expected_result, str(ex.exception))

    def test_drive(self):
        self.car.refuel(25)
        self.car.drive(100)
        self.assertEqual(19.4, self.car.fuel_amount)


if __name__ == '__main__':
    main()
