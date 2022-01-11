from math import floor

record_in_seconds = float(input())
distance = float(input())
seconds_per_meter = float(input())

distance_time = distance * seconds_per_meter
additional_time = floor(distance / 50) * 30    # Забавя го на всеки 50 метра с по 30 секунди
total_time = distance_time + additional_time

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    difference = total_time - record_in_seconds
    print(f"No! He was {difference:.2f} seconds slower.")