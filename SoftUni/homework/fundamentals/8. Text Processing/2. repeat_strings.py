text = input().split()
repeat = ""

for el in text:
    repeat += el * len(el)
print(repeat)