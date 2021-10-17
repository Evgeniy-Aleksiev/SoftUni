from math import floor
from collections import deque


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_seconds_from_time(time):
    hours, minutes, seconds = [int(x) for x in time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds):
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = []
robots_input = input().split(";")
products = deque()

for currents_robot in robots_input:
    robot_name, process_time = currents_robot.split('-')
    robots.append(Robot(robot_name, int(process_time)))

time_in_seconds = get_seconds_from_time(input())
product = input()

while not product == 'End':
    products.append(product)
    product = input()

while products:
    current_product = products.popleft()
    time_in_seconds += 1
    found_robot = False

    for robot in robots:

        if time_in_seconds >= robot.busy_until:
            robot.busy_until = time_in_seconds + robot.processing_time
            found_robot = True
            print(f"{robot.name} - {current_product} [{get_time_from_seconds(time_in_seconds)}]")
            break
    if not found_robot:
        products.append(current_product)