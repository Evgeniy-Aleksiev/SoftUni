activation_key = input()
data = input()

while not data == "Generate":
    command = data.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])

        if command[1] == "Upper":
            old_key = activation_key[start_index:end_index]
            new_key = activation_key[start_index:end_index].upper()
            activation_key = activation_key.replace(old_key, new_key)
        elif command[1] == "Lower":
            old_key = activation_key[start_index:end_index]
            new_key = activation_key[start_index:end_index].lower()
            activation_key = activation_key.replace(old_key, new_key)

        print(activation_key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])

        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    data = input()

print(f"Your activation key is: {activation_key}")

