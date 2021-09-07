numbers = [int(num) for num in input().split(", ")]

positive_numbers = [str(num) for num in numbers if num >= 0]
negative_numbers = [str(num) for num in numbers if num < 0]
even_numbers = [str(num) for num in numbers if num % 2 == 0]
odd_numbers = [str(num) for num in numbers if not num % 2 == 0]


print(f'Positive: {", ".join(positive_numbers)}')
print(f'Negative: {", ".join(negative_numbers)}')
print(f'Even: {", ".join(even_numbers)}')
print(f'Odd: {", ".join(odd_numbers)}')