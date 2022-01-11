from collections import deque

green_light = int(input())
free_window = int(input())

line_of_cars = deque()
cars_counter = 0
crashed = False

command = input()

while command != "END":
    if command == "green":
        if line_of_cars:
            current_car = line_of_cars.popleft()
            seconds_left = green_light - len(current_car)
            while seconds_left > 0:
                cars_counter += 1
                if line_of_cars:
                    current_car = line_of_cars.popleft()
                    seconds_left -= len(current_car)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                car_was_hit_at = free_window + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[car_was_hit_at]}.")
                crashed = True
                break
    else:
        line_of_cars.append(command)
    command = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")