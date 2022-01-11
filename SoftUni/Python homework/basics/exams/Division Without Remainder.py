numbers = int(input())

divided_2 = 0
divided_3 = 0
divided_4 = 0

for num in range(numbers):
    nums = int(input())
    if nums % 2 == 0:
        divided_2 += 1
    if nums % 3 == 0:
        divided_3 += 1
    if nums % 4 == 0:
        divided_4 += 1

print(f"{(divided_2 / numbers * 100):.2f}%")
print(f"{(divided_3 / numbers * 100):.2f}%")
print(f"{(divided_4 / numbers * 100):.2f}%")