
try:
    numbers_list = [int(x) for x in input().split(", ")]
except ValueError:
    print('Invalid input. Enter only numbers.')
    numbers_list = [int(x) for x in input().split(", ")]

result = 1

for number in numbers_list:
    if 0 == number:
        print('Cannot divide by Zero.')
        continue
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)


try:
    a = int('a')
except ValueError:
    print('Invalid input. Enter only numbers.')
    a = int(input())

try:
    result = 2 / a
except ZeroDivisionError:
    print('Division by zero. Enter number bigger than 0')
    result = 2 / int(input())

try:
    list_of_numbers = [int(x) for x in input().split(', ')]
except ValueError:
    print("Oops! That was no valid number. Try again...")
    list_of_numbers = [int(x) for x in input().split(', ')]

num = int(input('Enter index: '))
try:
    print(list_of_numbers[num])
except IndexError:
    print(f'Index {num} out of range. Your list length {len(list_of_numbers)}')

try:
    print(spam)
except NameError:
    print("name 'spam' is not defined")

