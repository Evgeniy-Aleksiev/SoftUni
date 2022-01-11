import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Test', 1000, 100)

    def test_worker_is_initialised_correctly(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_is_worker_incremented_energy_after_the_rest(self):
        # Arrange
        self.assertEqual(100, self.worker.energy)
        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(101, self.worker.energy)

    def test_person_works_with_negative_energy_raises(self):
        worker = Worker('Test', 1000, -10)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_correctly_increased_salary(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_is_worker_energy_decreased_after_work(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_is_correct_worker_info(self):
        result = self.worker.get_info()
        expected_result = 'Test has saved 0 money.'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
