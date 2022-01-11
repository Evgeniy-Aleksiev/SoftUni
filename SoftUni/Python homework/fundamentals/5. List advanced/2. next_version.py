version = [int(num) for num in input().split(".")]

version[-1] += 1

if version[-1] > 9:
    version[-1] = 0
    version[1] += 1
    if version[1] > 9:
        version[1] = 0
        version[0] += 1


print(f"{version[0]}.{version[1]}.{version[-1]}")