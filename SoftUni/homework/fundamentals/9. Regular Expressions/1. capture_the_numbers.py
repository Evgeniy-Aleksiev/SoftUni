import re

text = input()
pattern = r"\d+"
captured_number = []

while text:
    captured_number.extend(re.findall(pattern, text))
    text = input()
print(*captured_number)
