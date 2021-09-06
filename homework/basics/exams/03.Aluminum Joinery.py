number_joinery = int(input())
size_joinery = input()
delivery_type = input()

valid_order = True
joinery_price = 0

if number_joinery < 10:
    valid_order = False
else:
    if size_joinery == "90X130":
        joinery_price += 110 * number_joinery
        if 30 < number_joinery < 60:
            joinery_price *= 0.95
        elif number_joinery > 60:
            joinery_price *= 0.92
    elif size_joinery == "100X150":
        joinery_price += 140 * number_joinery
        if 40 < number_joinery < 80:
            joinery_price *= 0.94
        elif number_joinery > 80:
            joinery_price *= 0.90
    elif size_joinery == "130X180":
        joinery_price += 190 * number_joinery
        if 20 < number_joinery < 50:
            joinery_price *= 0.93
        elif number_joinery > 50:
            joinery_price *= 0.88
    elif size_joinery == "200X300":
        joinery_price += 250 * number_joinery
        if 25 < number_joinery < 50:
            joinery_price *= 0.91
        elif number_joinery > 50:
            joinery_price *= 0.86
    if delivery_type == "With delivery":
        joinery_price += 60
    if number_joinery > 99:
        joinery_price *= 0.96

if valid_order:
    print(f"{joinery_price:.2f} BGN")
else:
    print("Invalid order")
