queries = []

for _ in range(int(input())):
    querie = input()

    if querie.startswith('1'):
        try:
            _, number = querie.split()
            queries.append(int(number))
        except ValueError:
            print('You need to enter a number.')

    elif querie.startswith('2'):
        try:
            queries.pop()
        except IndexError:
            print('There is no queries.')
    elif querie.startswith('3'):
        try:
            print(max(queries))
        except ValueError:
            print('There is no queries.')
    elif querie.startswith('4'):
        try:
            print(min(queries))
        except ValueError:
            print('There is no queries.')


if queries:
    rev_nums = []
    for _ in range(len(queries)):
        rev_nums.append(queries.pop())
    print(', '.join(map(str, rev_nums)))