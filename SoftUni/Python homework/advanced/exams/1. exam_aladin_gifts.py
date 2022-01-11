from collections import deque

presents ={
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

materials = [int(x) for x in input().split()]
magic_level_value = deque([int(x) for x in input().split()])

while materials and magic_level_value:
    material = materials.pop()
    magic_level = magic_level_value.popleft()

    total_present_sum = material + magic_level

    if total_present_sum < 100:
        if total_present_sum % 2 == 0:
            total_present_sum = (material * 2) + (magic_level * 3)
        else:
            total_present_sum *= 2

    if total_present_sum >= 500:
        total_present_sum //= 2

    if 100 <= total_present_sum < 200:
        presents['Gemstone'] += 1
    elif 200 <= total_present_sum < 300:
        presents['Porcelain Sculpture'] += 1
    elif 300 <= total_present_sum < 400:
        presents['Gold'] += 1
    elif 400 <= total_present_sum < 500:
        presents['Diamond Jewellery'] += 1


if (presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1) or (presents['Gold'] >= 1and presents['Diamond Jewellery'] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')

if magic_level_value:
    print(f'Magic left: {", ".join(map(str, magic_level_value))}')

{print(f"{name}: {count}") for name, count in sorted(presents.items()) if count >= 1}

