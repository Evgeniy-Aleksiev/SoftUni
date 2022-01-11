import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
chars = r"[A-Za-z]"
mirror_words = []
matched = re.finditer(pattern, text)
cnt_pairs = 0

for x in matched:
    cnt_pairs += 1

    first_group = x.group(2)
    second_group = x.group(5)
    second_group_reversed = second_group[::-1]

    if first_group == second_group_reversed:
        word = f"{first_group} <=> {second_group}"
        mirror_words.append(word)

if cnt_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{cnt_pairs} word pairs found!")

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")
