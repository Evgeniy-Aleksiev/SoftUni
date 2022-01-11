season = input()
type_group = input()
number_students = int(input())
nights = int(input())
price = 0
sport = " "

if season == "Winter":
    if type_group == "girls":
        sport = "Gymnastics"
        price = (number_students * 9.60) * nights
    elif type_group == "boys":
        sport = "Judo"
        price = (number_students * 9.60) * nights
    else:
        sport = "Ski"
        price = (number_students * 10) * nights
elif season == "Spring":
    if type_group == "girls":
        sport = "Athletics"
        price = (number_students * 7.20) * nights
    elif type_group == "boys":
        sport = "Tennis"
        price = (number_students * 7.20) * nights
    else:
        sport = "Cycling"
        price = (number_students * 9.50) * nights
elif season == "Summer":
    if type_group == "girls":
        sport = "Volleyball"
        price = (number_students * 15) * nights
    elif type_group == "boys":
        sport = "Football"
        price = (number_students * 15) * nights
    else:
        sport = "Swimming"
        price = (number_students * 20) * nights

if 10 <= number_students < 20:
    price *= 0.95
elif 20 <= number_students < 50:
    price *= 0.85
elif number_students >= 50:
    price *= 0.50

print(f"{sport} {price:.2f} lv.")