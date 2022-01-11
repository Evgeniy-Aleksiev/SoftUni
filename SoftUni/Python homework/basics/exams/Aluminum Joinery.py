number_joinery = int(input())
joinery_size = input()
delivery_method  = input()

if number_joinery < 10:
    print("Invalid order")
else:
    price_per_joinery = 0
    if joinery_size == "90X130":
        price_per_joinery = 110
        if 30 <= number_joinery < 60:
            price_per_joinery = (number_joinery * 110) * 0.95
        elif number_joinery >= 60:
            price_per_joinery = (number_joinery * 110) * 0.92
    elif joinery_size == "100X150":
        price_per_joinery = 140
        if 40 <= number_joinery < 80:
            price_per_joinery = (number_joinery * 140) * 0.94
        elif number_joinery >= 80:
            price_per_joinery = (number_joinery * 140) * 0.90
    elif joinery_size == "130X180":
        price_per_joinery = 190
        if 20 <= number_joinery < 50:
            price_per_joinery = (number_joinery * 190) * 0.93
        elif number_joinery >= 50:
            price_per_joinery = (number_joinery * 190) * 0.88
    elif joinery_size == "200X300":
        price_per_joinery = 250
        if 25 <= number_joinery < 50:
            price_per_joinery = (number_joinery * 250) * 0.91
        elif number_joinery >= 50:
            price_per_joinery = (number_joinery * 250) * 0.86
    if delivery_method == "With delivery":
        price_per_joinery += 60
    if number_joinery >= 100:
        price_per_joinery *= 0.96
    print(f"{price_per_joinery:.2f} BGN")