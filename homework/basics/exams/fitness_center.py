visited_the_gym = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0
for people in range(1, visited_the_gym + 1):
    command = input()
    if command == "Back":
        back += 1
        work_out += 1
    elif command == "Chest":
        chest += 1
        work_out += 1
    elif command == "Legs":
        legs += 1
        work_out += 1
    elif command == "Abs":
        abs += 1
        work_out += 1
    elif command == "Protein shake":
        protein_shake += 1
        protein += 1
    elif command == "Protein bar":
        protein_bar += 1
        protein += 1

percent_work_out = work_out / visited_the_gym * 100
percent_protein = protein / visited_the_gym * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_work_out:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")
