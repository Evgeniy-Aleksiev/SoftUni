def is_valid(some_text: str, index1: int, index2: int):
    if 0 <= index1 < len(some_text) and 0 <= index2 < len(some_text):
        return True
    return print("Invalid indices!")


text = input()

data = input()

while not data == "Finish":
    cmd = data.split()
    command = cmd[0]

    if command == "Replace":
        current_char = cmd[1]
        new_char = cmd[2]

        if current_char in text:
            text = text.replace(current_char, new_char)

        print(text)

    elif command == "Cut":
        start_index = int(cmd[1])
        end_index = int(cmd[2])

        if is_valid(text, start_index, end_index):
            text = text[:start_index] + text[end_index + 1:]
            print(text)

    elif command == "Make":
        case = cmd[1]

        if case == "Upper":
            text = text.upper()
        elif case == "Lower":
            text = text.lower()

        print(text)

    elif command == "Check":
        check = cmd[1]

        if check in text:
            print(f"Message contains {check}")
        else:
            print(f"Message doesn't contain {check}")

    elif command == "Sum":
        start_index = int(cmd[1])
        end_index = int(cmd[2])

        if is_valid(text, start_index, end_index):
            letters = text[start_index:end_index + 1]
            total_sum = sum([ord(letter) for letter in letters])

            print(total_sum)

    data = input()
