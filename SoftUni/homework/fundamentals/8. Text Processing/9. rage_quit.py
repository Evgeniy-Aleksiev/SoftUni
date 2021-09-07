text = input()

repeating_string = ""
current_str = ""
num = 0

for i in range(len(text)):
    if not text[i].isdigit():
        current_str += text[i].upper()
        continue

    if not i == (len(text) - 1) and text[i + 1].isdigit():
        num += int(text[i])
        continue

    num = int(text[i])
    repeating_string += current_str * num
    current_str = ""

print(f"Unique symbols used: {len(set(repeating_string))}\n{repeating_string}")
