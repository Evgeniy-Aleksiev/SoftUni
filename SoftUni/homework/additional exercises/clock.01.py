hour = 0
minutes = 0

while hour < 24:
    while minutes < 60:
        print(f"{hour}:{minutes}")
        minutes += 1
    hour += 1
    minutes = 0
