bottles_preparation = int(input())
total_preparation = bottles_preparation * 750
dishes = 0
pots = 0
enough_detergent = True
command = input()
current_number = 0
while command != "End":
    current_number += 1
    plates_number = int(command)
    if total_preparation >= 0:
        if current_number % 3 == 0:
            total_preparation -= (plates_number * 15)
            pots += plates_number
        else:
            total_preparation -= (plates_number * 5)
            dishes += plates_number
    if total_preparation < 0:
        enough_detergent = False
        break
    command = input()

if enough_detergent:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_preparation} ml.")
else:
    print(f"Not enough detergent, {abs(total_preparation)} ml. more necessary!")