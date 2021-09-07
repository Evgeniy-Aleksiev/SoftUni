def replace_ch_code(word: str):
    ch_code_str = ""
    new_word = []

    for ch in word:
        if ch.isdigit():
            ch_code_str += ch
        else:
            new_word.append(ch)

    char_code = chr(int(ch_code_str))
    new_word.insert(0, char_code)

    return new_word


def letters_switch(word: str):
    new_word = replace_ch_code(word)

    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return "".join(new_word)


message = input().split()

decipher = []

for current_word in message:
    decipher.append(letters_switch(current_word))

print(" ".join(decipher))