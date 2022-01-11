text = input().split(" | ")

words_and_definitions = {}

for elements in text:
    word, definition = elements.split(": ")

    if word not in words_and_definitions:
        words_and_definitions[word] = []

    words_and_definitions[word].append(definition)

test_words = input().split(" | ")
command = input()


if command == "Test":
    for test in test_words:
        if test in words_and_definitions:
            print(f"{test}:")
            x = sorted(words_and_definitions[test], key=len)
            x.reverse()
            for v in x:
                print(f' -{"".join(v)}')

elif command == "Hand Over":
    print(f"{' '.join(sorted(words_and_definitions))}")