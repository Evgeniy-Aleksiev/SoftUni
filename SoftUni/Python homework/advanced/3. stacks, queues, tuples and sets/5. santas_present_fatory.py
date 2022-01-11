from collections import deque

presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

boxes_values = [int(x) for x in input().split()]
magic_values = deque(map(int, input().split()))

crafted = {}

while boxes_values and magic_values:
    current_box = boxes_values.pop()
    current_magic = magic_values.popleft()
    result = current_box * current_magic

    if current_box == 0 and current_magic == 0:
        continue

    if current_box == 0:
        magic_values.appendleft(current_magic)
        continue

    if current_magic == 0:
        boxes_values.append(current_box)
        continue

    if result in presents:
        product = presents[result]
        if product not in crafted:
            crafted[product] = 0
        crafted[product] += 1
    else:
        if result < 0:
            boxes_values.append(current_box + current_magic)
        else:
            boxes_values.append(current_box + 15)

is_crafted = ('Doll' in crafted and 'Wooden train' in crafted) or\
              ('Teddy bear' in crafted and 'Bicycle' in crafted)

if is_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_values:
    print(f'Materials left: {", ".join(map(str, reversed(boxes_values)))}')
if magic_values:
    print(f'Magic left: {", ".join(map(str, magic_values))}')

for toy, count in sorted(crafted.items()):
    print(f"{toy}: {count}")
