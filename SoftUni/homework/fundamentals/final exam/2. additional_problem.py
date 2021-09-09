import re

n = int(input())
pattern = r"^(\$|\%)(?P<tag>[A-Z][a-z]{2,})(\1)\:\s(\[(?P<num1>[\d]+)\]\|)(\[(?P<num2>[\d]+)\]\|)(\[(?P<num3>[\d]+)\]\|)$"

for _ in range(n):
    message = input()
    is_valid = False

    for el in re.finditer(pattern, message):
        word = chr(int(el.group('num1'))) + chr(int(el.group('num2'))) + chr(int(el.group('num3')))
        print(f"{el.group('tag')}: {word}")
        is_valid = True

    if not is_valid:
        print("Valid message not found!")
