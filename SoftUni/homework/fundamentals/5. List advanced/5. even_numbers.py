list_of_numbers = [int(el) for el in input().split(", ")]
even_numbers = [index for index in range(len(list_of_numbers)) if list_of_numbers[index] % 2 == 0]
print(even_numbers)
