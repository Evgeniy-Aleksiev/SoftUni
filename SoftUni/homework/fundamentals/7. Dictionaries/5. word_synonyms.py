n = int(input())

synonyms = {}

for _ in range(1, n + 1):
    word = input()
    current_synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(current_synonym)

[print(f"{el} - {', '.join(synonyms[el])}") for (el) in synonyms]
