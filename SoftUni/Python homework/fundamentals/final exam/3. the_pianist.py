n = int(input())

pianist = {}

for _ in range(n):
    piece_name, composer_name, key_name = input().split("|")

    pianist[piece_name] = {"composer": composer_name, "key": key_name}

data = input()

while not data == "Stop":
    cmd = data.split("|")
    command = cmd[0]
    piece = cmd[1]

    if command == "Add":
        composer = cmd[2]
        key = cmd[3]

        if piece not in pianist:
            pianist[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

        else:
            print(f"{piece} is already in the collection!")

    elif command == "Remove":
        if piece in pianist:
            print(f"Successfully removed {piece}!")
            del pianist[piece]

        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = cmd[2]
        if piece in pianist:
            pianist[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    data = input()

for keys, value in sorted(pianist.items(), key=lambda kvp: (kvp[0], kvp[1]['composer'])):
    print(f"{keys} -> Composer: {value['composer']}, Key: {value['key']}")
