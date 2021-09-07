text = input()

new_text = ""

for index in range(len(text)):
    if index < 1:
        new_text += text[index]
    elif not text[index] == text[index - 1]:
        new_text += text[index]

print(new_text)