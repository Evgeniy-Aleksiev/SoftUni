def odd_ever_sum(number):
    even_sum = 0
    odd_sum = 0
    for index in number:
        current_number = int(index)
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()
odd_ever_sum(num)