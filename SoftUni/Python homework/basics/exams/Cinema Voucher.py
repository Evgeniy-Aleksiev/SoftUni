voucher_value = int(input())
command = input()

tickets = 0
other_products = 0

while command != "End":
    purchase = command
    letter_number = 0
    for letter in range(len(purchase)):
        letter_number += 1
    if letter_number > 8:
        letters = " "
        for index, value in enumerate(ascii(purchase)):
            if 1 <= index <= 2:
                letters += value
        ord(letters)
    else:
        pass
