hour = int(input())
minutes = int(input())
minutes += 15

hour += minutes // 60
minutes %= 60

if hour > 23:
    hour -= 24
if minutes < 9:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")