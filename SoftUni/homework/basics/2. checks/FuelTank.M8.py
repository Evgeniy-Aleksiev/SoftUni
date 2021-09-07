fuel_type = input()
fuel_liters = float(input())

if fuel_type == 'Diesel' or fuel_type == 'Gas' or fuel_type == 'Gasoline':
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
