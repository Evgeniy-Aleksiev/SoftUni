def its_valid(collection: list, index: int, current_index: int):
    if 0 <= index + current_index < len(collection):
        return index
    index = 0
    return index


def cupid_jump(collection: list, index: int):
    if collection[index] <= 0:
        print(f"Place {index} already had Valentine's day.")
    elif collection[index] > 0:
        collection[index] -= 2
        if collection[index] == 0:
            print(f"Place {index} has Valentine's day.")


neighborhood = [int(num) for num in input().split("@")]
command = input()
jump_position = 0

while not command == "Love!":
    jump_index = int(command.split()[1])

    if its_valid(neighborhood, jump_index, jump_position) == 0:
        jump_position = 0
    else:
        jump_position += its_valid(neighborhood, jump_index, jump_position)
    cupid_jump(neighborhood, jump_position)

    command = input()

print(f"Cupid's last position was {jump_position}.")
count_v_days = neighborhood.count(0)

if count_v_days == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - count_v_days} places.")