actor_name = input()
academy_points = float(input())
number_jury = int(input())

reach_the_points = False
for jury in range(number_jury):
    jury_name = input()
    jury_points = float(input())
    letter_count = 0
    for letter in range(len(jury_name)):
        letter_count += 1
    academy_points += letter_count * jury_points / 2
    if academy_points >= 1250.5:
        reach_the_points = True
        break

if reach_the_points:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {round(academy_points, 1)}!")
else:
    points_need = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {round(points_need, 1)} more!")
