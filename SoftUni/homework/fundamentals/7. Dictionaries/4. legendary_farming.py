materials = input().split()

weapon = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
obtained = False

while not obtained:
    for index in range(0, len(materials), 2):
        if obtained:
            break
        quantity = int(materials[index])
        item = materials[index + 1].lower()
        if item in key_materials:
            key_materials[item] += quantity
            if key_materials[item] >= 250:
                key_materials[item] -= 250
                obtained = True
        else:
            if item not in junk_materials:
                junk_materials[item] = 0
            junk_materials[item] += quantity
        if obtained:
            for key, value in weapon.items():
                if item == key:
                    print(f"{value} obtained!")
                    break
    if obtained:
        break
    materials = input().split()
order = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for key, value in order:
    print(f"{key}: {value}")

junk_items = sorted(junk_materials.items(), key=lambda kvp: kvp[0])
for key, value in junk_items:
    print(f"{key}: {value}")

