number = int(input())
combination = 0
for x1 in range(number +1):
    for x2 in range(number +1):
        for x3 in range(number +1):
            if x1 + x2 + x3 == number:
                combination += 1
print(combination)
