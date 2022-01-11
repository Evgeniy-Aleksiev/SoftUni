symbols = {',', '.', '?', '"', "'", "!", ':', ';', '-', '_'}

with open('text.txt', 'r') as file:
    index = 1

    for el in file:
        letters_cnt = 0
        symbols_cnt = 0

        for ch in el:
            if ch in symbols:
                symbols_cnt += 1
            elif ch.isalpha():
                letters_cnt += 1

        with open('output.txt', 'a') as f:
            text = f'Line {index}: {el.strip()} ({letters_cnt})({symbols_cnt})\n'
            f.write(text)

        index += 1
