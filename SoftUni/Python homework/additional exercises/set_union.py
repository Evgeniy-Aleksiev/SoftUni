n, english_newspaper = int(input()), set(input().split())
b, french_newspaper = int(input()), set(input().split())
p = len(english_newspaper.union(french_newspaper))
print(p)

