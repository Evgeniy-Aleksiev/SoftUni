wagon_number = [0 for x in range(int(input()))]
command = input()

while not command == "End":
    commands = command.split()
    index = int(commands[1])
    if commands[0] == "add":
        wagon_number[-1] += int(commands[1])
    elif commands[0] == "insert":
        wagon_number[index] += int(commands[2])
    elif commands[0] == "leave":
        wagon_number[index] -= int(commands[2])

    command = input()

print(wagon_number)

