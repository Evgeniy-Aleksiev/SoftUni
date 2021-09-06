n = int(input())

print('*' * (2 * n) + ' ' * n + '*' * (2 * n))
for i in range(n - 2):
    print('*' + (2 * n - 2) * '/' + '*', end='')
    if i == (n - 1) // 2 - 1:
        print('|' * n, end='')
    else:
        print(' ' * n, end='')
    print('*' + (2 * n - 2) * '/' + '*')
print('*' * (2 * n) + ' ' * n + '*' * (2 * n))