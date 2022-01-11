quantity_eggs = int(input())
command = input()
not_enough_eggs = False

sold_eggs = 0
while command != 'Close':
    eggs_number = int(input())
    if command == "Buy":
        if quantity_eggs < eggs_number:
            not_enough_eggs = True
            break
        else:
            quantity_eggs -= eggs_number
            sold_eggs += eggs_number
    elif command == "Fill":
        quantity_eggs += eggs_number

    command = input()

if command == 'Close':
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
if not_enough_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {quantity_eggs}.")