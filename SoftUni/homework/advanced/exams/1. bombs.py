from collections import deque

bombs_cnt = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0
}



bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

while bomb_effects and bomb_casings:
    if all(value >= 3 for value in bombs_cnt.values()):
        break

    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casings = bomb_casings.pop()


    while not last_bomb_casings < 0:
        sum_of_values = first_bomb_effect + last_bomb_casings
        if sum_of_values == 40:
            bombs_cnt['Datura Bombs'] += 1
            break
        if sum_of_values == 60:
            bombs_cnt['Cherry Bombs'] += 1
            break
        if sum_of_values == 120:
            bombs_cnt['Smoke Decoy Bombs'] += 1
            break

        last_bomb_casings -= 5

if all(value >= 3 for value in bombs_cnt.values()):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join(map(str, bomb_effects))}')
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join(map(str, bomb_casings))}')
else:
    print('Bomb Casings: empty')

{print(f"{key}: {value}") for key, value in bombs_cnt.items()}