clients = int(input())

total_price = 0

for client in range(clients):
    command = input()
    number_purchase = 0
    final_price = 0
    while command != "Finish":
        number_purchase += 1
        if command == "basket":
            final_price += 1.50
        elif command == "wreath":
            final_price += 3.80
        elif command == "chocolate bunny":
            final_price += 7
        command = input()
    if number_purchase % 2 == 0:
        final_price *= 0.80
    total_price += final_price
    print(f"You purchased {number_purchase} items for {final_price:.2f} leva.")
print(f"Average bill per client is: {(total_price / clients):.2f} leva.")
