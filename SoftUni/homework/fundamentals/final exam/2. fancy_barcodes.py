import re

n = int(input())

pattern = r"\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+"
only_digits = r"\d"

for _ in range(n):
    text = input()
    x = re.match(pattern, text)
    if x is None:
        print("Invalid barcode")
    else:
        match = re.findall(only_digits, text)
        if len(match) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(match)}")

