from project.sports_car import SportsCar
from project.vehicle import Vehicle
from project.car import Car

vehicle = Vehicle()
print(f'From class Vehivle: {vehicle.move()}.')
print()
car = Car()
print(f'From class Car: {car.move()} {car.drive()}.')
print()
sport_car = SportsCar()
print(f'From class SportCar: {sport_car.move()} {sport_car.drive()} {sport_car.race()}.')