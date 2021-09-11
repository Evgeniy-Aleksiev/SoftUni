start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
combination = 0
found = False

for x1 in range(start_of_interval, end_of_interval + 1):
    for x2 in range(start_of_interval, end_of_interval + 1):
        combination += 1
        if x1 + x2 == magic_number:
            found = True
            print(f"Combination N:{combination} ({x1} + {x2} = {magic_number})")
            break
    if found:
        break
if not found:
    print(f"{combination} combinations - neither equals {magic_number}")
