from collections import deque

formed_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow'],
}

main_colors = {'red', 'blue', 'yellow'}
secondary_colors = {'orange', 'purple', 'green'}

substring = deque(input().split())
colors = []

while substring:
    left = substring.popleft()
    right = substring.pop() if substring else ''
    color = left + right

    if color in main_colors or color in secondary_colors:
        colors.append(color)
        continue

    color = right + left
    if color in main_colors or color in secondary_colors:
        colors.append(color)
        continue
    else:
        left = left[:-1]
        right = right[:-1]

        if left:
            substring.insert(len(substring) // 2, left)
        if right:
            substring.insert(len(substring) // 2, right)

for el in colors:
    if el in main_colors:
        continue
    required_colors = formed_colors[el]
    is_valid = all([x in colors for x in required_colors])
    if is_valid:
        continue
    colors.remove(el)

print(colors)

