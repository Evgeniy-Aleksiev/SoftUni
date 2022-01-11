text = input()

if ":" in text:
    for index in range(len(text)):
        if text[index] == ":":
            current_emoji = text[index] + text[index + 1]
            print(current_emoji)


