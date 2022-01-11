import re

symbol = input()
symbols_not_read = ""
letter = ""
secret_symbol_n = 0
secret_symbol_o = 0
secret_symbol_c = 0

while symbol != "End":
    for symbol in range(a, z):
        if secret_symbol_n != 0 and secret_symbol_o != 0 and secret_symbol_c != 0:
            letter += symbols_not_read
            secret_symbol_n = 0
            secret_symbol_o = 0
            secret_symbol_c = 0
            symbols_not_read = " "

        if symbol != "n" and symbol != "o" and symbol != "c":
            symbols_not_read += symbol

        if symbol == "n":
            if secret_symbol_n == 0:
                secret_symbol_n += 1
            else:
                symbols_not_read += symbol
        elif symbol == "o":
            if secret_symbol_o == 0:
                secret_symbol_o += 1
            else:
                symbols_not_read += symbol
        elif symbol == "c":
            if secret_symbol_c == 0:
                secret_symbol_c += 1
            else:
                symbols_not_read += symbol
        symbol = input()

print(chr(letter))
