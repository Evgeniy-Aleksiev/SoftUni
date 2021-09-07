vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
text_without_vowels = [el for el in input() if el not in vowels]
print("".join(text_without_vowels))