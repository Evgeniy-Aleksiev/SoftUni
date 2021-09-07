gifts = input().split()
command = input()

while not command == "No Money":
    current_command = command.split()
    value_command = current_command[0]
    gift_command = current_command[1]

    if value_command == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == gift_command:
                gifts[index] = "None"

    elif value_command == "Required":
        index_command = int(current_command[2])
        if 0 <= index_command < len(gifts):
            gifts[index_command] = gift_command

    elif value_command == "JustInCase":
        gifts[-1] = gift_command

    command = input()

for gift in gifts:
    if not gift == "None":
        print(gift, end=" ")