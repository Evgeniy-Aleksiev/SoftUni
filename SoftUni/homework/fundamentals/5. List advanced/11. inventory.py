def collect(collection: list, item: str):
    if item not in collection:
        collection.append(item)

    return collection


def drop(collection: list, item: str):
    if item in collection:
        collection.remove(item)

    return collection


def combine_items(collection: list, old_item: str, new_item: str):
    index = collection.index(old_item)
    collection.insert(index + 1, new_item)


def renew(collection: list, item: str):
    if item in collection:
        index = collection.index(item)
        catch_item = collection.pop(index)
        collection.append(catch_item)
    return collection


collecting_items = [item for item in input().split(", ")]

command = input()

while not command == "Craft!":
    cmd, cmd_item = command.split(" - ")

    if cmd == "Collect":
        collect(collecting_items, cmd_item)
    elif cmd == "Drop":
        drop(collecting_items, cmd_item)
    elif cmd == "Combine Items":
        old, new = cmd_item.split(":")
        if old in collecting_items:
            combine_items(collecting_items, old, new)
    elif cmd == "Renew":
        renew(collecting_items, cmd_item)

    command = input()

print(", ".join(collecting_items))
