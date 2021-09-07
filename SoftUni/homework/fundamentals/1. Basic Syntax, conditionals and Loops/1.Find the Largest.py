number = list(input())
number.sort(reverse=True)
for current_number in range(len(number)):
    print(number[current_number], end="")