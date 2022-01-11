day_off = int(input())

rest = day_off * 127
work_day = 365
work_day -= day_off
work_day_time = work_day * 63
total_time = rest + work_day_time
difference = abs(30000 - total_time)
hour = difference // 60
minutes = difference % 60

if total_time > 30000:
    print("Tom will run away")
    print(f"{hour} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hour} hours and {minutes} minutes less for play")