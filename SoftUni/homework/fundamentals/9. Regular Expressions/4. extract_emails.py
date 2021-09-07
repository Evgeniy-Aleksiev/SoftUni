import re

text = input()
pattern = r"\s(?P<Email>(?P<User>[A-Za-z0-9]+([\.\-\_A-Za-z]+)*@)(?P<host>[A-Za-z]+[\-[A-Za-z]+]*(\.[A-Za-z]+)+))"
matches = re.finditer(pattern, text)
[print(match.group("Email")) for match in matches]
