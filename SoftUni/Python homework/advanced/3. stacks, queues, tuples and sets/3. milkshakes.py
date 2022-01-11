from collections import deque

chocolate = input().split(', ')  # starting from the last
cups_of_milk = deque(input().split(', '))

milkshakes_count = 0

while chocolate and cups_of_milk and milkshakes_count < 5:

    chocolate_value = int(chocolate.pop())
    milk_value = int(cups_of_milk.popleft())

    if milk_value <= 0 and chocolate_value <= 0:
        continue

    if milk_value <= 0:
        chocolate.append(str(chocolate_value))
        continue

    if chocolate_value <= 0:
        cups_of_milk.appendleft(str(milk_value))
        continue

    if chocolate_value == milk_value:
        milkshakes_count += 1

    else:
        cups_of_milk.append(str(milk_value))
        chocolate_value -= 5
        chocolate.append(str(chocolate_value))

if milkshakes_count >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(chocolate)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(cups_of_milk)}")
else:
    print("Milk: empty")
