events = input().split("|")

initial_energy = 100
initial_coins = 100
bankrupt = False

for event in events:
    current_event = event.split("-")
    event_type = current_event[0]
    event_number = int(current_event[1])

    if event_type == "rest":
        if initial_energy + event_number > 100:
            print("You gained 0 energy.")
        else:
            initial_energy += event_number
            print(f"You gained {event_number} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == "order":
        if initial_energy - 30 >= 0:
            initial_energy -= 30
            initial_coins += event_number
            print(f"You earned {event_number} coins.")

        else:
            if initial_energy + 50 <= 100:
                initial_energy += 50
            else:
                initial_energy = 100
            print("You had to rest!")

    else:
        if initial_coins > event_number:
            initial_coins -= event_number
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            bankrupt = True
            break

if not bankrupt:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
