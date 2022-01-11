first_number = int(input())
second_number = int(input())

for number_one in range(1, first_number + 1):
    for number_two in range(1, first_number + 1):
        for letter_one in range(97, 97 + second_number):
            for letter_two in range(97, 97 + second_number):
                for number_three in range(1, first_number + 1):
                    if number_three > number_one and number_three > number_two:
                        print(f"{number_one}{number_two}{chr(letter_one)}{chr(letter_two)}{number_three}", end=" ")
