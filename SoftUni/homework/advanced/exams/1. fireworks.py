from collections import deque

fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0
}

firework_effect = deque([int(x) for x in input().split(', ') if 0 < int(x)])
explosive_power = [int(x) for x in input().split(', ') if 0 < int(x)]

while firework_effect and explosive_power:
    current_firework_effect = firework_effect.popleft()
    current_explosive_power = explosive_power[-1]
    sum_of_values = current_firework_effect + current_explosive_power

    if sum_of_values % 3 == 0 and sum_of_values % 5 == 0:
        fireworks['Crossette'] += 1
    elif sum_of_values % 5 == 0:
        fireworks['Willow'] += 1
    elif sum_of_values % 3 == 0:
        fireworks['Palm'] += 1
    else:
        if current_firework_effect > 1:
            firework_effect.append(current_firework_effect - 1)
        continue

    explosive_power.pop()

    if all(x >= 3 for x in fireworks.values()):
        break

if all(x >= 3 for x in fireworks.values()):
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effect:
    print(f"Firework Effects left: {', '.join(map(str, firework_effect))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

{print(f'{name} Fireworks: {count}')for name, count in fireworks.items()}