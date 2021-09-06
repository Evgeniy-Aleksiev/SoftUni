# При тръгването има определен брой пътници
# На всяка спирка слизат определен брой пътници
# На всеки нечетен брой спирки се качват по 2ма проверяващи и слизат на четните
# Общия брой пътници на последната спирка

number_of_passengers = int(input())
number_of_stops = int(input())


for stops in range(1, number_of_stops +1):
    disembarking_passengers = int(input())
    number_of_passengers -= disembarking_passengers
    boarding_passengers = int(input())
    number_of_passengers += boarding_passengers

    if stops % 2 == 0:  # Когато е четно слизат 2ма проверяващи
        number_of_passengers -= 2
    else:                           # Когато е нечетно се качват 2ма проверяващи
        number_of_passengers += 2

print(f"The final number of passengers is : {number_of_passengers}")