symbols = {"-", ",", ".", "!", "?"}

with open('text.txt', 'r+') as file:
    for index, line in enumerate(file):

        if not index % 2 == 0:
            index += 1
            continue

        for symbol in symbols:
            line = line.replace(symbol, '@')
        line = ' '.join(line.split()[::-1])
        print(line)
        index += 1