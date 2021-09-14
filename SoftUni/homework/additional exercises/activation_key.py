text = input()
data = input()

while not data == "Generate":
    cmd = data.split(">>>")

    if cmd[0] == "Contains":
        substring = cmd[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif cmd[0] == "Flip":
        start_index, end_index = int(cmd[2]), int(cmd[3])
        substring = text[start_index:end_index]

        if cmd[1] == "Upper":
            text = text[:start_index] + substring.upper() + text[end_index:]
        elif cmd[1] == "Lower":
            text = text[:start_index] + substring.lower() + text[end_index:]

        print(text)

    elif cmd[0] == "Slice":
        start_index, end_index = int(cmd[1]), int(cmd[2])
        text = text[:start_index] + text[end_index:]
        print(text)

    data = input()

print(f"Your activation key is: {text}")
