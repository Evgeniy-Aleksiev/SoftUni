numbers = [int(num) for num in input().split(", ")]
y = 10

while numbers:
    group = [num for num in numbers if num <= y]
    for el in group:
        numbers.remove(el)
    print(f"Group of {y}'s: {group}")
    y += 10
