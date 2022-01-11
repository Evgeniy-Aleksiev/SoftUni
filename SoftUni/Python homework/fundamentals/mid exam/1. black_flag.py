days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plumber = 0

for current_day in range(1, days +1):
    total_plumber += plunder_per_day
    if current_day % 3 == 0:
        total_plumber += plunder_per_day / 2

    if current_day % 5 == 0:
        total_plumber -= total_plumber * 0.30

if total_plumber >= expected_plunder:
    print(f"Ahoy! {total_plumber:.2f} plunder gained.")
else:
    percentage = total_plumber / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
