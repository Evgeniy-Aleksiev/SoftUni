import re

with open('word.txt') as file:
    searched_words = file.read().split()

words_contained = {}

with open('input.txt') as file:
    contain = file.read()
    for word in searched_words:
        pattern = rf'(\-|\s|\b){word}(\.|\,|\s|\!|\?\b)'
        result = re.findall(pattern, contain, re.IGNORECASE)
        if word not in words_contained:
            words_contained[word] = len(result)

sorted_list = sorted(words_contained.items(), key=lambda x: -x[-1])
with open('output.txt', 'a') as file:
    for current_word, count in sorted_list:
        text = f'{current_word} - {count}\n'
        file.write(text)
