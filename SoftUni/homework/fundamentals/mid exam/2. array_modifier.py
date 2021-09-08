def its_valid(collection: list, index1: int, index2: int):
    if 0 <= index1 < len(collection) and 0 <= index2 < len(collection):
        return True
    return False


def swap(collection: list, index1: int, index2: int):
    if its_valid(collection, index1, index2):
        collection[index1], collection[index2] = collection[index2], collection[index1]

    return collection


def multiply(collection: list, index1: int, index2: int):
    if its_valid(collection, index1, index2):
        result = collection[index1] * collection[index2]
        collection[index1] = result

    return collection


def decrease(collection: list):
    for index in range(len(collection)):
        collection[index] -= 1

    return collection


array_values = [int(x) for x in input().split()]
command = input()

while not command == "end":
    split = command.split()
    cmd = split[0]

    if cmd == "swap":
        cmd_index1 = int(split[1])
        cmd_index2 = int(split[2])
        swap(array_values, cmd_index1, cmd_index2)
    elif cmd == "multiply":
        cmd_index1 = int(split[1])
        cmd_index2 = int(split[2])
        multiply(array_values, cmd_index1, cmd_index2)
    elif cmd == "decrease":
        decrease(array_values)

    command = input()

str_list = [str(x) for x in array_values]
print(', '.join(str_list))
