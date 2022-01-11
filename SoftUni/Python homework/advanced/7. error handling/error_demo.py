# Some text
text = 'Hello'

try:
    number = int(input())
    result = text * number
    print(2 / number)
except ValueError as Error:
    print(Error)
except ZeroDivisionError:
    print('Division by zero')