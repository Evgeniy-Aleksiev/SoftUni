def cupid_jumps(collection: list, index: int):
    if collection[index] > 0:
        collection[index] -= 2
        if collection[index] == 0:
            print(f"Place {index} has Valentine's day." )
    else:
        print(f"Place {index} already had Valentine's day.")


neighborhood = [int(current) for current in input().split("@")]

command = input()
current_index = 0

while not command == "Love!":
    jump, cmd_index = command.split()
    current_index += int(cmd_index)
    if current_index < len(neighborhood):
        cupid_jumps(neighborhood, current_index)
    else:
        current_index = 0
        cupid_jumps(neighborhood, current_index)

    command = input()

print(f"Cupid's last position was {current_index}.")
count_of_celebrate = neighborhood.count(0)

if count_of_celebrate == len(neighborhood):
    print(f"Mission was successful.")

else:
    not_celebrate = abs(count_of_celebrate - len(neighborhood))
    print(f"Cupid has failed {not_celebrate} places.")
