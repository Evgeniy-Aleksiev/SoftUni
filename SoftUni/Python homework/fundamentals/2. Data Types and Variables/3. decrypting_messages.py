key = int(input())
n = int(input())

for letters in range(n):
    current_letter = input()
    letter = ord(current_letter) + key
    print(chr(letter), end="")