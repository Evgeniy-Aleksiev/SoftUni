a1 = int(input())
a2 = int(input())
n = int(input())

for symbol1 in range(a1, a2):
    for symbol2 in range(1, n):
        for symbol3 in range(1, n):
            number_symbol = symbol3 // 2
            if symbol1 % 2 == 1 and (symbol2 + number_symbol + symbol1) % 2 == 1:
                letter = chr(symbol1)
                print(f"{letter}-{symbol2}{number_symbol}{symbol1}")
