from collections import deque

cars_queue = deque()
green_light = int(input())
free_window = int(input())
command = input()
passed_cars = 0
crash = False

while not command == 'END':
    time_left = green_light

    if command == 'green':
        if cars_queue:
            for _ in range(len(cars_queue)):
                current_car = cars_queue.popleft()
                if time_left > 0:
                    if len(current_car) <= time_left + free_window:
                        passed_cars += 1
                        time_left -= len(current_car)
                    else:
                        hitted_car_index = abs(time_left) + free_window
                        print(f'A crash happened!')
                        print(f'{current_car} was hit at {current_car[hitted_car_index]}.')
                        crash = True
                        break
    else:
        cars_queue.append(command)
    if crash:
        break
    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")