pair_number = int(input())
pair_sum2 = 0
max_diff = 0
number1 = int(input())
number2 = int(input())
pair_sum = number1 + number2

for pair in range(1, pair_number):
    number1 = int(input())
    number2 = int(input())

    if pair % 2 == 1:
        pair_sum2 = number1 + number2
    else:
        pair_sum = number1 + number2

    if max_diff < abs(pair_sum - pair_sum2):
        max_diff = abs(pair_sum - pair_sum2)

if max_diff == 0:
    print(f"Yes, value={pair_sum}")
else:
    print(f"No, maxdiff={max_diff}")