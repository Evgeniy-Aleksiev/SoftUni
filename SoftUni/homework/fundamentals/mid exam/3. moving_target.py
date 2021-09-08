def its_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True
    return False


def shoot(collection: list, index: int, power: int):
    if its_valid(collection, index):
        collection[index] -= power

        if collection[index] <= 0:
            collection.pop(index)

    return collection


def add(collection: list, index: int, value: int):
    if its_valid(collection, index):
        collection.insert(index, value)
        return collection

    return print("Invalid placement!")


def strike(collection: list, index: int, radius: int):
    left_strike_index = index - radius
    right_strike_index = index + radius
    if its_valid(collection, left_strike_index) and \
            its_valid(collection, index) and \
            its_valid(collection, right_strike_index):

        del collection[left_strike_index:right_strike_index + 1]
    else:
        print("Strike missed!")

    return collection


sequence_of_targets = [int(x) for x in input().split()]
command = input()

while not command == "End":
    cmd, cmd_index, cmd_value = command.split()

    if cmd == "Shoot":
        shoot(sequence_of_targets, int(cmd_index), int(cmd_value))
    elif cmd == "Add":
        add(sequence_of_targets, int(cmd_index), int(cmd_value))
    elif cmd == "Strike":
        strike(sequence_of_targets, int(cmd_index), int(cmd_value))

    command = input()

str_targets = [str(x) for x in sequence_of_targets]
print('|'.join(str_targets))
