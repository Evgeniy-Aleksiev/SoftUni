text = input()
data = input()

new_word = ""

while not data == "Done":
    command = data.split()

    if command[0] == "TakeOdd":
        for i in range(len(text)):
            if not i % 2 == 0:
                new_word += text[i]
        text = new_word
        new_word = ""
        print(text)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2]) + index
        text = text[:index] + text[length:]
        print(text)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

    data = input()

print(f"Your password is: {text}")
