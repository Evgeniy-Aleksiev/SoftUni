command = input()

reverse_string = {}

while not command == "end":
    reverse_string[command] = command[::-1]

    command = input()

[print(f"{key} = {value}") for (key, value) in reverse_string.items()]