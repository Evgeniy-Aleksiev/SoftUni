n = int(input())

even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

for _ in range(n):
    number = int(input())

    if number % 2 == 0:
        even_numbers.append(number)
    if number % 2 == 1:
        odd_numbers.append(number)
    if number >= 0:
        positive_numbers.append(number)
    if number < 0:
        negative_numbers.append(number)

command = input()

if command == "even":
    print(even_numbers)
elif command == "odd":
    print(odd_numbers)
elif command == "positive":
    print(positive_numbers)
elif command == "negative":
    print(negative_numbers)