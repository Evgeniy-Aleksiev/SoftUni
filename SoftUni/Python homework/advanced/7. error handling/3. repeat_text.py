text = input()

try:
    result = text * int(input())
except ValueError:
    print('Variable times must be an integer')
