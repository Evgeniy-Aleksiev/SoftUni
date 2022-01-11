rows_count, columns_count = [int(x) for x in input().split()]

for r in range(rows_count):
    for c in range(columns_count):
        print(f'{chr(97 + r)}{chr(97 + r+ c)}{chr(97 + r)}', end=' ')
    print()