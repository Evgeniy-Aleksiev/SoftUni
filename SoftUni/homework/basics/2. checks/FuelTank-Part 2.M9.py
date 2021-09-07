type_fuel = input()
quantity_fuel = float(input())
club_card = input()

if type_fuel == "Gasoline":
    price_fuel = quantity_fuel * 2.22
    if club_card == "Yes":
        price_fuel -= quantity_fuel * 0.18

elif type_fuel == "Diesel":
    price_fuel = quantity_fuel * 2.33
    if club_card == "Yes":
        price_fuel -= quantity_fuel * 0.12

elif type_fuel == "Gas":
    price_fuel = quantity_fuel * 0.93
    if club_card == "Yes":
        price_fuel -= quantity_fuel * 0.08

if 20 <= quantity_fuel <= 25:
    price_fuel -= 0.08 * price_fuel
elif quantity_fuel > 25:
    price_fuel -= 0.10 * price_fuel

print(f"{price_fuel:.2f} lv.")