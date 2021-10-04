def char_combination(text, idx=0):
    if idx >= len(text):
        print(''.join(text))
        return

    char_combination(text, idx+1)
    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        char_combination(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


char_combination(list(input()))