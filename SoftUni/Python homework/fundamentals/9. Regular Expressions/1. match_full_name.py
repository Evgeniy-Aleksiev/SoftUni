import re

expression = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
name = input()
print(" ".join(re.findall(expression, name)))