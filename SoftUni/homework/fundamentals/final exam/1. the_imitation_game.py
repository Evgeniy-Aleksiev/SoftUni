message = input()

data = input()

while not data == "Decode":
    cmd = data.split("|")
    command = cmd[0]

    if command == "Move":
        n = int(cmd[1])

        first_letters = message[:n]
        message = message[n:] + first_letters

    elif command == "Insert":
        index = int(cmd[1])
        value = cmd[2]

        message = message[:index] + value + message[index:]

    elif command == "ChangeAll":
        substring = cmd[1]
        replacement = cmd[2]

        message = message.replace(substring, replacement)

    data = input()

print(f"The decrypted message is: {message}")
