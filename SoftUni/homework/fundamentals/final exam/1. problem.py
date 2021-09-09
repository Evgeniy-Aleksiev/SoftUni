text = input()

data = input()

while not data == "End":
    cmd = data.split()
    command = cmd[0]

    if command == "Translate":
        char = cmd[1]
        replacement = cmd[2]

        text = text.replace(char, replacement)
        print(text)

    elif command == "Includes":
        word = cmd[1]

        print(bool(word in text))

    elif command == "Start":
        word = cmd[1]

        print(bool(text.startswith(word)))

    elif command == "Lowercase":
        text = text.lower()

        print(text)

    elif command == "FindIndex":
        char = cmd[1]

        for index in range(len(text)-1, -1, -1):
            if text[index] == char:
                print(index)
                break

    elif command == "Remove":
        start_index = int(cmd[1])
        count = int(cmd[2])

        end = start_index + count
        text = text[:start_index] + text[end:]

        print(text)

    data = input()

