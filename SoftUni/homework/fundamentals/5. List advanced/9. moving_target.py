def is_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True

    return False


def command_shoot(collection: list, index: int, power: int):

    if is_valid(collection, index):
        if collection[index] > power:
            collection[index] -= power
        else:
            collection.pop(index)

    return collection


def command_add(collection: list, index: int, value: int):
    if is_valid(collection, index):
        collection.insert(index, value)

        return collection

    return print("Invalid placement!")


def command_strike(collection: list, strike_index: int, radius: int):
    left_strike_index = strike_index - radius
    right_strike_index = strike_index + radius

    if is_valid(collection, left_strike_index) and \
            is_valid(collection, strike_index) and \
            is_valid(collection, right_strike_index):

        del collection[left_strike_index:right_strike_index +1]

    else:
        print("Strike missed!")

    return collection


sequence_of_targets = [int(num) for num in input().split()]

command = input()

while not command == "End":
    cmd_type, cmd_index, cmd_value = command.split()

    if cmd_type == "Shoot":
        command_shoot(sequence_of_targets, int(cmd_index), int(cmd_value))

    elif cmd_type == "Add":
        command_add(sequence_of_targets, int(cmd_index), int(cmd_value))

    elif cmd_type == "Strike":
        command_strike(sequence_of_targets, int(cmd_index), int(cmd_value))

    command = input()

numbers_str_list = [str(num) for num in sequence_of_targets]
print('|'.join(numbers_str_list))
