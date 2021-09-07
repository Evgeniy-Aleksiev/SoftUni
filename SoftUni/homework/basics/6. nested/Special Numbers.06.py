number = int(input())

for special_number in range(1111, 10000):
    number_is_special = True
    for index, value in enumerate(str(special_number)):
        current_value = int(value)
        if current_value == 0 or number % current_value != 0:
            number_is_special = False
            break
    if number_is_special:
        print(special_number, end=" ")
