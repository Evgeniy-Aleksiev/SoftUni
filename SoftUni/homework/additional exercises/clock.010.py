hour = 0

while hour < 24:
    for minutes in range(60):
        for seconds in range(60):
            print(f"{hour}:{minutes:0>2d}:{seconds:0>2d}")
    hour += 1