dungeon_rooms = input().split('|')

initial_health = 100
initial_bitcoins = 0

died = False

for current_room in range(1, len(dungeon_rooms) + 1):
    command, number = dungeon_rooms[current_room - 1].split()
    number = int(number)

    if command == "potion":
        if initial_health < 100:
            if initial_health + number > 100:
                amount = 100 - initial_health
                initial_health = 100
                print(f"You healed for {amount} hp.")
            else:
                initial_health += number
                print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")

    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        if number < initial_health:
            initial_health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.\nBest room: {current_room}")
            died = True
            break

if not died:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")
