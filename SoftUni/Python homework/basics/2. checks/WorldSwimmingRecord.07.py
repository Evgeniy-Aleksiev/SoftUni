record = float(input())
distance = float(input())
per_second_distance = float(input())

swim = distance * per_second_distance
water_slow = int(distance / 15) * 12.5
total_time = swim + water_slow
time_left = total_time - record

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_left:.2f} seconds slower.")