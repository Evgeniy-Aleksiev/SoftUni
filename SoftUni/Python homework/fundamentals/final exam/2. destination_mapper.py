import re

text = input()
pattern = r"(=|/)([A-Z][A-Za-z]{2,})(\1)"

total_points = 0
match = re.finditer(pattern, text)
valid_locations = []

for x in match:
    total_points += len(x.group(2))
    valid_locations.append(x.group(2))

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {total_points}")
