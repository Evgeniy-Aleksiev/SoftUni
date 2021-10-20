from collections import deque

fireworks_type = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0
}

def perfect_firework_show():
    return all(x >= 3 for x in fireworks_type.values())

def mix_fireworks(firework, explosive):
    firework_queue = deque([x for x in firework if x > 0])
    explosive_stack = [x for x in explosive if x > 0]

    while firework_queue and explosive_stack and not perfect_firework_show():
        current_firework = firework_queue.popleft()
        current_explosive = explosive_stack.pop()
        sum_of_values = current_firework + current_explosive

        if sum_of_values % 5 == 0 and sum_of_values % 3 == 0:
            fireworks_type['Crossette'] += 1
        elif sum_of_values % 3 == 0:
            fireworks_type['Palm'] += 1
        elif sum_of_values % 5 == 0:
            fireworks_type['Willow'] += 1
        else:
            if current_firework > 1:
                firework_queue.append(current_firework - 1)
            explosive_stack.append(current_explosive)

    return firework_queue, explosive_stack


firework_effects = [int(x) for x in input().split(', ')]
explosive_power = [int(x) for x in input().split(', ')]
firework, explosive = mix_fireworks(firework_effects, explosive_power)

if perfect_firework_show():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework:
    print(f"Firework Effects left: {', '.join(map(str, firework))}")
if explosive:
    print(f"Explosive Power left: {', '.join(map(str, explosive))}")
for firework_name, firework_count in fireworks_type.items():
    print(f"{firework_name} Fireworks: {firework_count}")
