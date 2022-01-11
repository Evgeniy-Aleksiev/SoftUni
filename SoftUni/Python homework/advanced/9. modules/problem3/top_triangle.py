def top_side_of_triangle(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()

def down_side_of_triangle(n):
    for row in range(n, 0, - 1):
        for col in range(1, row):
            print(col, end=' ')
        print()
