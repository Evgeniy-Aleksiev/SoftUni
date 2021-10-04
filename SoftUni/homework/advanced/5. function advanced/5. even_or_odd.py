def even_odd(*args):
    command = args[-1]
    com = 1 if command == 'odd' else 0
    numbers = []

    for num in args[0: len(args) - 1]:
        if num % 2 == com:
            numbers.append(num)

    return numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
