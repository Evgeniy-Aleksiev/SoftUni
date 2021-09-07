import re

pattern = r"(?P<url>www\.(?P<domain>[A-Za-z0-9]+[\-A-Za-z0-9]*)(?P<extension>(\.[a-z]+)+))"
text = input()

while not text == "":
    matched = re.finditer(pattern, text)
    [print(match.group("url")) for match in matched]
    text = input()

