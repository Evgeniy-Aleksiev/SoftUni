def is_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True
    return False


def defending_index(collection: list, start_index: int, end_index: int):
    if 0 <= start_index < len(collection) and 0 <= end_index < len(collection):
        return True
    return False


def fire(collection: list, index: int, damage: int):
    if is_valid(collection, index):
        collection[index] -= damage
        if collection[index] <= 0:
           return True


def defend(collection:list, star_index: int, end_index: int, damage: int):
    if defending_index(collection, star_index, end_index):
        for i in range(star_index, end_index + 1):
            collection[i] -= damage
            if collection[i] <= 0:
                return True


def repair(collection: list, index: int, health: int, max_health: int):
    if is_valid(collection, index):
        if collection[index] + health <= max_health:
            collection[index] += health
        elif collection[index] < max_health:
            collection[index] = max_health


def status(collection: list, max_health: int):
    count = 0
    for i in range(len(collection)):
        if collection[i] / max_health * 100 < 20:
            count += 1
    return count


# Ships status
pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]

# Maximum health capacity each ship
maximum_health_capacity = int(input())

command = input()
stalemate = True

while not command == "Retire":
    cmd = command.split()
    if cmd[0] == "Fire":
        if fire(warship, int(cmd[1]), int(cmd[2])):
            print("You won! The enemy ship has sunken.")
            stalemate = False
            break
    elif cmd[0] == "Defend":
        if defend(pirate_ship, int(cmd[1]), int(cmd[2]), int(cmd[3])):
            print("You lost! The pirate ship has sunken.")
            stalemate = False
            break
    elif cmd[0] == "Repair":
        repair(pirate_ship, int(cmd[1]), int(cmd[2]), maximum_health_capacity)
    elif cmd[0] == "Status":
        repair_ships_cnt = status(pirate_ship, maximum_health_capacity)
        print(f"{repair_ships_cnt} sections need repair.")

    command = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
