from unittest import TestCase, main
from project.pet_shop import PetShop


class PetShopTest(TestCase):
    PET_SHOP_NAME = 'Pet Shop'
    FOOD_NAME = 'test_food'
    PET_NAME = 'Gosho'

    def setUp(self) -> None:
        self.pet_shop = PetShop(self.PET_SHOP_NAME)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.PET_SHOP_NAME, self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_quantity_equal_or_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food(self.FOOD_NAME, -1)

        expected_result = 'Quantity cannot be equal to or less than 0'
        self.assertEqual(expected_result, str(ve.exception))

    def test_add_food_if_name_not_in_food(self):
        self.pet_shop.add_food(self.FOOD_NAME, 1)
        self.pet_shop.add_food('another', 15)

        self.assertEqual(1, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual(15, self.pet_shop.food['another'])

    def test_add_food_name_in_food_expect_to_increase_quantity(self):
        self.pet_shop.add_food(self.FOOD_NAME, 1)
        self.assertEqual(1, self.pet_shop.food[self.FOOD_NAME])
        self.pet_shop.add_food(self.FOOD_NAME, 12)
        self.assertEqual(13, self.pet_shop.food[self.FOOD_NAME])

    def test_add_food__when_food_not_in_petshop__expect_correct_message(self):
        quantity = 10
        result = self.pet_shop.add_food(self.FOOD_NAME, quantity)
        expected_result = f'Successfully added {quantity:.2f} grams of {self.FOOD_NAME}.'

        self.assertEqual(expected_result, result)

    def test_add_pet_expect_append_name_of_pet(self):
        result = self.pet_shop.add_pet(self.PET_NAME)
        self.assertTrue(self.PET_NAME in self.pet_shop.pets)

        expected_return = f"Successfully added {self.PET_NAME}."
        self.assertEqual(expected_return, result)

    def test_add_pet_expect_raise_exception(self):
        self.pet_shop.add_pet(self.PET_NAME)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(self.PET_NAME)

        expected_result = 'Cannot add a pet with the same name'
        self.assertEqual(expected_result, str(ex.exception))

    def test_feed_pet_raise_exception(self):
        self.assertTrue(self.PET_NAME not in self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        expected_result = 'Please insert a valid pet name'
        self.assertEqual(expected_result, str(ex.exception))

    def test_feed_pet_food_name_not_in_food(self):
        expected_message = f'You do not have {self.FOOD_NAME}'
        self.pet_shop.add_pet(self.PET_NAME)
        self.assertFalse(self.FOOD_NAME in self.pet_shop.food)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)
        self.assertEqual(expected_message, result)

    def test_feed_pet_when_food_is_99_expect_to_incr_by_1000(self):
        food_quantity = 99
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_food(self.FOOD_NAME, food_quantity)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)
        self.assertEqual(food_quantity + 1000, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual('Adding food...', result)

    def test_feed_pet_when_food_is_101_expect_to_decrease_by_100(self):
        food_quantity = 101
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_food(self.FOOD_NAME, food_quantity)

        result = self.pet_shop.feed_pet(self.FOOD_NAME, self.PET_NAME)

        self.assertEqual(food_quantity - 100, self.pet_shop.food[self.FOOD_NAME])
        self.assertEqual( f'{self.PET_NAME} was successfully fed', result)

    def test_repr_when_no_pets_expect_correct_result(self):
        expected = f'''Shop {self.PET_SHOP_NAME}:
Pets: '''

        actual = repr(self.pet_shop)

        self.assertEqual(
            expected,
            actual
        )

    def test__repr_when_to_single_pet__expect_correct_result(self):
        self.pet_shop.add_pet(self.PET_NAME)
        expected_result = f'''Shop {self.PET_SHOP_NAME}:
Pets: {self.PET_NAME}'''

        actual = repr(self.pet_shop)
        self.assertEqual(expected_result, actual)

    def test__repr_when_to_multiple_pets__expect_correct_result(self):
        another_pet_name = self.PET_NAME + '2'
        self.pet_shop.add_pet(self.PET_NAME)
        self.pet_shop.add_pet(another_pet_name)

        expected = f'''Shop {self.PET_SHOP_NAME}:
Pets: {self.PET_NAME}, {another_pet_name}'''
        actual = repr(self.pet_shop)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    main()

