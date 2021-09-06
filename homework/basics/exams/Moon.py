import math

average_speed = float(input())
fuel_litters_100m = float(input())

total_distance = 384400 * 2
time_round_trip = math.ceil(total_distance / average_speed)
total_time = time_round_trip + 3
fuel = fuel_litters_100m * total_distance / 100

print(total_time)
print(int(fuel))