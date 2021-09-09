all_stops = input()

data = input()


def is_valid(text: str, i: int):
    if 0 <= i < len(text):
        return True
    return False


while not data == "Travel":
    cmd = data.split(":")
    command = cmd[0]

    if command.startswith("Add"):
        index = int(cmd[1])
        city = cmd[2]
        if is_valid(all_stops, index):
            all_stops = all_stops[:index] + city + all_stops[index:]

        print(all_stops)

    elif command.startswith("Remove"):
        starting_index = int(cmd[1])
        end_index = int(cmd[2])

        if is_valid(all_stops, starting_index) and is_valid(all_stops, end_index):
            all_stops = all_stops[:starting_index] + all_stops[end_index + 1:]

        print(all_stops)
    elif command == "Switch":
        old_string = cmd[1]
        new_string = cmd[2]

        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)

        print(all_stops)

    data = input()

print(f"Ready for world tour! Planned stops: {all_stops}")
