first_number = int(input())
second_number = int(input())

number1 = " "
number2 = " "
for index, vaLue in enumerate(str(first_number)):
    current_number = int(vaLue)
    if current_number % 2 == 1:
        number1 += vaLue
for index, vaLue in enumerate(str(second_number)):
    current_number = int(vaLue)
    if current_number % 2 == 1:
        number2 += vaLue

for first_number_barcode in range(int(number1, number2 +1)):
        print(first_number_barcode)