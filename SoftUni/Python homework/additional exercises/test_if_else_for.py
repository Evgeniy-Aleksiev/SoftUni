n = 10
a = 5
b = 0

for x in range(n):
    b += 1
    if b >= a:
        print('b >= a')
    else:
        print('b < a')