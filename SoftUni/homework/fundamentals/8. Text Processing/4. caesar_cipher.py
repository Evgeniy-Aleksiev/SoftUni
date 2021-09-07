word = input()
new_word = ""

for index in range(len(word)):
    new_word += chr(ord(word[index]) + 3)

print(new_word)
