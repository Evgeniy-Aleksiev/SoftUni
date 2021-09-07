first_chr = int(input())
second_chr = int(input())

for current_chr in range(first_chr, second_chr + 1):
    characters = chr(current_chr)
    print(characters, end=" ")