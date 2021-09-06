eggs_size = input()
egg_colour = input()
number_batches = int(input())

per_batches = 0
if eggs_size == "Large":
    if egg_colour == "Red":
        per_batches += 16
    elif egg_colour == "Green":
        per_batches += 12
    elif egg_colour == "Yellow":
        per_batches += 9
elif eggs_size == "Medium":
    if egg_colour == "Red":
        per_batches += 13
    elif egg_colour == "Green":
        per_batches += 9
    elif egg_colour == "Yellow":
        per_batches += 7
elif eggs_size == "Small":
    if egg_colour == "Red":
        per_batches += 9
    elif egg_colour == "Green":
        per_batches += 8
    elif egg_colour == "Yellow":
        per_batches += 5

total_price = per_batches * number_batches
tax = total_price - total_price * 0.35

print(f"{tax:.2f} leva.")