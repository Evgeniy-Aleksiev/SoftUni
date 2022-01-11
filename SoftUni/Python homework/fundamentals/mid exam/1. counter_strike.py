initial_energy = int(input())
command = input()

win_count = 0
game_over = False

while not command == "End of battle":
    enemy_distance = int(command)

    if initial_energy >= enemy_distance:
        win_count += 1
        initial_energy -= enemy_distance
        if win_count % 3 == 0:
            initial_energy += win_count

    elif initial_energy <= 0 or initial_energy < enemy_distance:
        print(f"Not enough energy! Game ends with {win_count} won battles and {initial_energy} energy")
        game_over = True
        break

    command = input()

if not game_over:
    print(f"Won battles: {win_count}. Energy left: {initial_energy}" )
