def collect(item: str):
    if item not in collecting_items:
        collecting_items.append(item)


def drop(item: str):
    if item in collecting_items:
        collecting_items.remove(item)


def combine_items(item: str):
    old_item, new_item = item.split(":")
    if old_item in collecting_items:
        index = collecting_items.index(old_item)
        collecting_items.insert(index + 1, new_item)


def renew(item: str):
    if item in collecting_items:
        index = collecting_items.index(item)
        catch = collecting_items.pop(index)
        collecting_items.append(catch)


collecting_items = input().split(", ")
command = input()

while not command == "Craft!":
    cmd, cmd_items = command.split(" - ")

    if cmd == "Collect":
        collect(cmd_items)
    elif cmd == "Drop":
        drop(cmd_items)
    elif cmd == "Combine Items":
        combine_items(cmd_items)
    elif cmd == "Renew":
        renew(cmd_items)

    command = input()

print(', '.join(collecting_items))
