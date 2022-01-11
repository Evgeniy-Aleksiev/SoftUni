n = int(input())
word = input()

list_of_strings = []
specific_word_in_list = []

for x in range(n):
    text = input()
    list_of_strings.append(text)

    if word in text:
        specific_word_in_list.append(text)

print(list_of_strings)
print(specific_word_in_list)