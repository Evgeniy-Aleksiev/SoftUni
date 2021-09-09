secret_chat = input()

data = input()

while not data == "Reveal":
    cmd = data.split(":|:")
    command = cmd[0]

    if command == "InsertSpace":
        index = int(cmd[1])

        secret_chat = secret_chat[:index] + " " + secret_chat[index:]
        print(secret_chat)

    elif command == "Reverse":
        substring = cmd[1]
        if substring in secret_chat:
            secret_chat = secret_chat.replace(substring, '', 1)
            secret_chat += substring[::-1]
            print(secret_chat)
        else:
            print("error")
    elif command == "ChangeAll":
        substring, replacement = cmd[1], cmd[2]
        secret_chat = secret_chat.replace(substring, replacement)
        print(secret_chat)
    data = input()

print(f"You have a new text message: {secret_chat}")
