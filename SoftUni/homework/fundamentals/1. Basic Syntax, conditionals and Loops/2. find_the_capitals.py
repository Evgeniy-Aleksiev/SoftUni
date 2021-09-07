text = input()
upper = []

for x in range(len(text)):
    if text[x].isupper():
        upper.append(x)
print(upper)