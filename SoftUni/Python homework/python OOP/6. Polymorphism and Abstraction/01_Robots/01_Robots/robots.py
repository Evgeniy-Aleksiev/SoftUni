# Variant 1

class Robot:
    _sensors_amount = 1

    def __init__(self, name):
        self.name = name

    @classmethod
    def sensors_amount(cls):
        return cls._sensors_amount


class MedicalRobot(Robot):
    _sensors_amount = 6


class ChefRobot(Robot):
    _sensors_amount = 4


class WarRobot(Robot):
    _sensors_amount = 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(moley)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(griffin)


# Variant 2
print('\n-------------------------\n')


class Robot2:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot2(Robot2):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot2(Robot2):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot2(Robot2):
    @staticmethod
    def sensors_amount():
        return 12


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


basic_robot2 = Robot2('Robo')
da_vinci2 = MedicalRobot2('Da Vinci')
moley2 = ChefRobot2('Moley')
griffin2 = WarRobot2('Griffin')

number_of_robot_sensors(basic_robot2)
number_of_robot_sensors(moley2)
number_of_robot_sensors(da_vinci2)
number_of_robot_sensors(griffin2)
