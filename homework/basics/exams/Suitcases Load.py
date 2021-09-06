capacity_storage = float(input())
storage_is_full = False
suitcase = 0
taken = 0
command = input()

while command != "End":
    suitcase_volume = float(command)
    taken += suitcase_volume
    if taken >= capacity_storage:
        storage_is_full = True
        break
    suitcase += 1
    if suitcase % 3 == 0:
        suitcase_volume += 0.1 * suitcase_volume
    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")
elif storage_is_full:
    print("No more space!")
print(f"Statistic: {suitcase} suitcases loaded.")