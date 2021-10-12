from collections import deque


def is_valid(r, c, board):
    if 0 <= r < len(board) and 0 <= c < len(board[row]):
        return True
    return False


def attack(r, c, board, destroyed_count):
    if board[r][c] > 0:
        board[r][c] -= 1
        if board[r][c] == 0:
            destroyed_count += 1

    return destroyed_count


battle_field = []

for row in range(int(input())):
    battle_ships = [int(x) for x in input().split()]
    battle_field.append(battle_ships)

attack_coordinates = deque(input().split())
destroyed_ships = 0

while attack_coordinates:
    attack_row, attack_col = attack_coordinates.popleft().split('-')
    attack_row, attack_col = int(attack_row), int(attack_col)
    if is_valid(attack_row, attack_col, battle_field):
        destroyed_ships = attack(attack_row, attack_col, battle_field, destroyed_ships)

print(destroyed_ships)