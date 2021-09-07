substring_remove = input()
text = input()

while substring_remove in text:
    text = text.replace(substring_remove, "")

print(text)