def combinations(chars, index=0):
    if len(chars) <= index:
        print(''.join(chars))
        return

    combinations(chars, index + 1)
    for i in range(index +1, len(chars)):
        chars[index], chars[i] = chars[i], chars[index]
        combinations(chars, index+1)
        chars[index], chars[i] = chars[i], chars[index]


combinations(list(input()))