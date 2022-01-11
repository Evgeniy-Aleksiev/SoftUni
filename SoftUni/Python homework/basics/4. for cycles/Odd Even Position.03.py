import sys

n = int(input())
odd_max_number = -sys.maxsize
odd_min_number = sys.maxsize
odd_sum = 0
even_sum = 0
even_max_number = -sys.maxsize
even_min_number = sys.maxsize

for number in range(1, n + 1):
    current_number = float(input())
    if number % 2 == 0:
        even_sum += current_number
        if current_number > even_max_number:
            even_max_number = current_number
        if current_number < even_min_number:
            even_min_number = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max_number:
            odd_max_number = current_number
        if current_number < odd_min_number:
            odd_min_number = current_number

print(f"OddSum={odd_sum:.2f},")
if odd_min_number == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min_number:.2f},")
if odd_max_number == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max_number:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min_number == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min_number:.2f},")
if even_max_number == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max_number:.2f}")