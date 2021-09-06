first_match_result = input()
second_match_result = input()
third_match_result = input()

wins = 0
lose = 0
drawn = 0

letter = first_match_result[0]
letter2 = first_match_result[2]
if letter > letter2:
    wins += 1
elif letter == letter2:
    drawn += 1
else:
    lose += 1
letter = second_match_result[0]
letter2 = second_match_result[2]
if letter > letter2:
    wins += 1
elif letter == letter2:
    drawn += 1
else:
    lose += 1
letter = third_match_result[0]
letter2 = third_match_result[2]
if letter > letter2:
    wins += 1
elif letter == letter2:
    drawn += 1
else:
    lose += 1

print(f"Team won {wins} games.")
print(f"Team lost {lose} games.")
print(f"Drawn games: {drawn}")