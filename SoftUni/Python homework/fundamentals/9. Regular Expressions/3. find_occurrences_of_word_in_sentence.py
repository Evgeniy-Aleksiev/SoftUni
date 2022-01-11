import re

text = input()
word = input()
pattern = rf'\b{word}\b'
matched = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(matched))

# два вида решение на задачата

text = input().lower()
word = input().lower()
pattern = rf'\b{word}\b'
matched = re.findall(pattern, text)
print(len(matched))