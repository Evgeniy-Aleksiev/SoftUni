cards = input().split()
count_shuffle = int(input())

half_cards = len(cards) // 2

for i in range(1, count_shuffle + 1):
    left_half = cards[:half_cards]
    right_half = cards[half_cards:]
    current_shuffle = []

    for j in range(len(left_half)):
        current_shuffle.append(left_half[j])
        current_shuffle.append(right_half[j])

    cards = current_shuffle

print(cards)