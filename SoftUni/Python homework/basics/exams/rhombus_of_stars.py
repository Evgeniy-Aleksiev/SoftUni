number = int(input())

for i in range(1, number +1):
    print(" " * (number - i) + "* " * i)
for j in range(1, number + 1):
    print(" " * j + "* " * (number - j))