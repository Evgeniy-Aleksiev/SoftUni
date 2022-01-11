n = int(input())

discovered = {}
plants_len = {}

for _ in range(n):
    cmd = input().split("<->")
    plant_name, plant_rarity = cmd[0], int(cmd[1])

    if plant_name not in discovered:
        discovered[plant_name] = {'rarity': 0, 'rating': 0}
        plants_len[plant_name] = 0

    discovered[plant_name]['rarity'] += plant_rarity

command = input()

while not command == "Exhibition":
    com, pln = command.split(": ")

    if com == "Rate":
        plant, rating = pln.split(" - ")
        rating = int(rating)

        if plant not in discovered:
            print("error")
            command = input()
            continue

        discovered[plant]['rating'] += rating
        plants_len[plant] += 1

    elif com == "Update":
        plant, new_rarity = pln.split(" - ")
        new_rarity = int(new_rarity)

        if plant not in discovered:
            print("error")
            command = input()
            continue

        discovered[plant]['rarity'] = new_rarity

    elif com == "Reset":
        if pln not in discovered:
            print("error")
            command = input()
            continue

        discovered[pln]['rating'] = 0
        plants_len[pln] = 0

    command = input()

for key, value in discovered.items():
    a = discovered[key]['rating']
    if a > 0:
        discovered[key]['rating'] = a / plants_len[key]


print("Plants for the exhibition:")
for key, value in sorted(discovered.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['rating'])):
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")
