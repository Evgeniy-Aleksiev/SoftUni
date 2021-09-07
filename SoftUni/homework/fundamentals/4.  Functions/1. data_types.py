def data_types(command: str, text: str):
    if command == "int":
        print(2 * int(text))

    elif command == "real":
        print(f"{1.5 * float(text):.2f}")

    elif command == "string":
        print("$" + text + "$")


command_input = input()
text_input = input()

data_types(command_input, text_input)
