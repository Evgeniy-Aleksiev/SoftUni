club_name = input()
played_matches = int(input())

points = 0
w = 0
d = 0
l = 0

for matches in range(played_matches):
    result = input()
    if result == "W":
        points += 3
        w += 1
    elif result == "D":
        points += 1
        d += 1
    elif result == "L":
        l += 1

if played_matches < 1:
    print(f"{club_name} hasn't played any games during this season.")
else:
    print(f"{club_name} has won {points} points during this  season.")
    print("Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {w / played_matches * 100:.2f}%")
