def urgent(item: str):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item: str):
    if item in initial_list:
        initial_list.remove(item)


def correct(old_item: str, new_item: str):
    if old_item in initial_list:
        index = initial_list.index(old_item)
        initial_list.remove(old_item)
        initial_list.insert(index, new_item)


def rearrange(item: str):
    if item in initial_list:
        index = initial_list.index(item)
        catch = initial_list.pop(index)
        initial_list.append(catch)


initial_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    cmd = command.split()

    if cmd[0] == "Urgent":
        urgent(cmd[-1])
    elif cmd[0] == "Unnecessary":
        unnecessary(cmd[-1])
    elif cmd[0] == "Correct":
        correct(cmd[1], cmd[-1])
    elif cmd[0] == "Rearrange":
        rearrange(cmd[-1])

    command = input()

print(", ".join(initial_list))
