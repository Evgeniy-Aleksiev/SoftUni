import re

text = input()

emoji_detector = r"(\*\*|\:\:)([A-Z][a-z]{2,})(\1)"
digit_detector = r"\d"

coolness = {}
cool_threshold = 1
threshold = re.finditer(emoji_detector, text)
cool_thresh = re.finditer(digit_detector, text)

for element in threshold:
    el = element.group()
    el_points = 0
    for i in range(2, len(el)-2):
        el_points += ord(el[i])
    coolness[el] = el_points

for d in cool_thresh:
    cool_threshold *= int(d.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{len(coolness)} emojis found in the text. The cool ones are:")
[print(key) for key, value in coolness.items() if value >= cool_threshold]

