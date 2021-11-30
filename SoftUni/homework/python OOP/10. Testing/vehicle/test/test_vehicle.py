from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20, 150)

    def test_vehicle_init_create_all_attributes(self):
        self.assertEqual(20, self.vehicle.fuel)
        self.assertEqual(20, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(600)

        expected_result = 'Not enough fuel'
        self.assertEqual(expected_result, str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_refuel_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)

        expected_result = 'Too much fuel'
        self.assertEqual(expected_result, str(ex.exception))

    def test_refuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(12.5, self.vehicle.fuel)

    def test_return_info(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                          f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == '__main__':
    main()