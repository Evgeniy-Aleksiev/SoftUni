first_word = input()
second_word = input()
third_word = first_word
for symbol in range(len(first_word)):
    left_side = second_word[:symbol +1]
    right_side = first_word[symbol +1:]
    current_word = left_side + right_side
    if current_word == third_word:
        continue
    print(current_word)
    third_word = current_word