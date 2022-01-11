number_balls = int(input())

total_points = 0
red_ball = 0
orange_ball = 0
yellow_ball = 0
white_ball = 0
black_ball = 0
other_balls = 0

for colours in range(1, number_balls +1):
    colour = input()
    if colour == "red":
        total_points += 5
        red_ball += 1
    elif colour == "orange":
        total_points += 10
        orange_ball += 1
    elif colour == "yellow":
        total_points += 15
        yellow_ball += 1
    elif colour == "white":
        total_points += 20
        white_ball += 1
    elif colour == "black":
        total_points /= 2
        black_ball += 1
    else:
        other_balls += 1

print(f"Total points: {int(total_points)}")
print(f"Points from red balls: {red_ball}")
print(f"Points from orange balls: {orange_ball}")
print(f"Points from yellow balls: {yellow_ball}")
print(f"Points from white balls: {white_ball}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_ball}")