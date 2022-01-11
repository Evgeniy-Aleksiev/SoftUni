factor = int(input())
count = int(input())

multiples_list = []

for current_number in range(1, count + 1):
    multiple = factor * current_number
    multiples_list.append(multiple)
print(multiples_list)