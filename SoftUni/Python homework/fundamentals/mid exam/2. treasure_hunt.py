def is_valid(collection: list, cmd_index: int):
    if 0 <= cmd_index < len(collection):
        return True
    return False


def drop(collection: list, cmd_index: int):
    if is_valid(collection, cmd_index):
        catch = collection.pop(cmd_index)
        collection.append(catch)


def steal(collection: list, count: int):
    stolen_items = []
    if count < len(collection):
        for i in range(count):
            stolen_items.insert(0, collection[-1])
            collection.remove(collection[-1])
        print(', '.join(stolen_items))
    else:
        stolen_items.extend(collection)
        collection.clear()
        print(', '.join(stolen_items))
        return collection


initial_loot = input().split("|")
data = input()

while not data == "Yohoho!":
    command = data.split()
    if command[0] == "Loot":
        for index in range(1, len(command)):
            if command[index] not in initial_loot:
                initial_loot.insert(0, command[index])
    elif command[0] == "Drop":
        drop(initial_loot, int(command[1]))

    elif command[0] == "Steal":
        steal(initial_loot, int(command[1]))

    data = input()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = sum([len(el) for el in initial_loot]) / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
