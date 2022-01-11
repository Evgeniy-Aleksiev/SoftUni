from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Aleksiev', 60, 10000, 1250)

    def test_hero_init_create_all_attributes(self):
        self.assertEqual('Aleksiev', self.hero.username)
        self.assertEqual(60, self.hero.level)
        self.assertEqual(10000, self.hero.health)
        self.assertEqual(1250, self.hero.damage)

    def test_hero_info(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_result, str(self.hero))

    def test_battle_vs_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        expected_result = 'You cannot fight yourself'
        self.assertEqual(expected_result, str(ex.exception))

    def test_hero_health_zero_or_negative(self):
        for health in [0, -25]:
            hero = Hero('Al', 60, health, 1250)
            with self.assertRaises(Exception) as ex:
                hero.battle(self.hero)

            expected_result = 'Your health is lower than or equal to 0. You need to rest'
            self.assertEqual(expected_result, str(ex.exception))

    def test_enemy_hero_health_zero_or_negative(self):
        for health in [0, -25]:
            hero = Hero('Al', 60, health, 1250)
            with self.assertRaises(Exception) as ex:
                self.hero.battle(hero)

            expected_result = f'You cannot fight {hero.username}. He needs to rest'
            self.assertEqual(expected_result, str(ex.exception))

    def test_draw_battle(self):
        enemy_hero = Hero('Al', 60, 10000, 1250)
        expected_health = self.hero.health - enemy_hero.level * enemy_hero.damage

        actual = self.hero.battle(enemy_hero)
        self.assertEqual('Draw', actual)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_health, enemy_hero.health)

    def test_you_win_when_enemy_dies(self):
        enemy_hero = Hero('Al', 60, 2000, 100)
        expected_enemy_health = enemy_hero.health - self.hero.level * self.hero.damage
        expected_hero_health = self.hero.health - enemy_hero.level * enemy_hero.damage
        actual = self.hero.battle(enemy_hero)

        self.assertEqual('You win', actual)
        self.assertEqual(expected_enemy_health, enemy_hero.health)
        self.assertEqual(61, self.hero.level)
        self.assertEqual(expected_hero_health + 5, self.hero.health)
        self.assertEqual(1255, self.hero.damage)

    def test_lose_when_you_die(self):
        enemy_hero = Hero('Al', 60, 110000, 1250)
        expected_enemy_health = enemy_hero.health - self.hero.level * self.hero.damage
        expected_hero_health = self.hero.health - enemy_hero.level * enemy_hero.damage
        actual = self.hero.battle(enemy_hero)

        self.assertEqual('You lose', actual)
        self.assertEqual(expected_enemy_health + 5, enemy_hero.health)
        self.assertEqual(61, enemy_hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(1255, enemy_hero.damage)


if __name__ == '__main__':
    main()
