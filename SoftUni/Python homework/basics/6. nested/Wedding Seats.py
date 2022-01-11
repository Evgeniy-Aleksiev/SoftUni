first = input()
s = int(input())
t = int(input())

f = ord(first)
total_sits = 0


for symbol in range(65, f + 1):
    for sectors in range(1, s + 1):
        odd = False
        if sectors % 2 == 0:
            odd = True
            t += 2
        sit_letter = 97
        for sits in range(1, t + 1):
            total_sits += 1
            sector_symbol = chr(symbol)
            current_sit = chr(sit_letter)
            print(f"{sector_symbol}{sectors}{current_sit}")
            sit_letter += 1
        if odd:
            t -= 2
    s += 1
print(total_sits)