number = int(input())

print("+", end=" ")
for i in range(number - 2):
    print("-", end=" ")
print("+", end=" ")
print()
for row in range(number - 2):
    print("|", end=" ")
    for col in range(number - 2):
        print("-", end=" ")
    print("|", end=" ")
    print()
print("+", end=" ")
for x in range(number - 2):
    print("-", end=" ")
print("+", end=" ")
print()
