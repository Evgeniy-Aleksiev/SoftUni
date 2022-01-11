import re

text = input()
pattern = r"\b_[A-Za-z0-9]+\b"
matched = re.findall(pattern, text)

variable_names = []

for match in matched:
    variable = match[1:]
    variable_names.append(variable)
print(",".join(variable_names))

