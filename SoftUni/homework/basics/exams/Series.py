budget = float(input())
number_of_serials = int(input())
total_price = 0
for serial in range(1, number_of_serials + 1):
    serial_name = input()
    serial_price = float(input())

    if serial_name == "Thrones":
        serial_price *= 0.50
    elif serial_name == "Lucifer":
        serial_price *= 0.60
    elif serial_name == "Protector":
        serial_price *= 0.70
    elif serial_name == "TotalDrama":
        serial_price *= 0.80
    elif serial_name == "Area":
        serial_price *= 0.90

    total_price += serial_price
difference = budget - total_price
if budget >= total_price:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {abs(difference):.2f} lv. more to buy the series!")
