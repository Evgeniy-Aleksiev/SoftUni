import re

date = input()
pattern = r"(?P<Day>\d{2})(?P<Separator>[.\-\/])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>(\d{4}))"
matches = [obj.groupdict() for obj in re.finditer(pattern, date)]
print("\n".join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in matches]))

