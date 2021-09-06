number_moves = int(input())
points = 0
invalid_number = 0
range_1 = 0
range_2 = 0
range_3 = 0
range_4 = 0
range_5 = 0


for moves in range(number_moves):
    moves = int(input())
    if 0 > moves or moves > 50:
        points /= 2
        invalid_number += 1
    elif moves < 10:
        points += moves * 0.20
        range_1 += 1
    elif moves < 20:
        points += moves * 0.30
        range_2 += 1
    elif moves < 30:
        points += moves * 0.40
        range_3 += 1
    elif moves < 40:
        points += 50
        range_4 += 1
    elif moves <= 50:
        points += 100
        range_5 += 1

print(f"{points:.2f}")
print(f"From 0 to 9: {(range_1 / number_moves * 100):.2f}%")
print(f"From 10 to 19: {(range_2 / number_moves * 100):.2f}%")
print(f"From 20 to 29: {(range_3 / number_moves * 100):.2f}%")
print(f"From 30 to 39: {(range_4 / number_moves * 100):.2f}%")
print(f"From 40 to 50: {(range_5 / number_moves * 100):.2f}%")
print(f"Invalid numbers: {(invalid_number / number_moves * 100):.2f}%")

