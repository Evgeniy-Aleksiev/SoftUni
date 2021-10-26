def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(1, n - 1):
        triangle.append([])
        triangle[-1].append(1)
        for col in range(row):
            left = triangle[row][col]
            right = triangle[row][col + 1]
            triangle[-1].append(left + right)
        triangle[-1].append(1)

    return triangle

print(get_magic_triangle(5))