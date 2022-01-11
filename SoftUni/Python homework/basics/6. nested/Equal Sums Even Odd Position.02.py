first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for index, value in enumerate(str(number)):
        if index % 2 == 0:
            even_sum += int(value)
        else:
            odd_sum += int(value)
    if even_sum == odd_sum:
        print(number, end=" ")