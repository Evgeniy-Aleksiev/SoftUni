def read_matrix():
    matrix = []
    rows_count, columns_count = [int(x) for x in input().split()]

    for current_row in range(rows_count):
        matrix.append(list(input().split()))

    return matrix, rows_count, columns_count


def identical_chr_count(matrix, rows_cnt, col_cnt):
    count = 0

    for r in range(rows_cnt - 1):
        for c in range(col_cnt - 1):

            if matrix[r][c] == matrix[r][c + 1] == \
                    matrix[r + 1][c] == matrix[r + 1][c + 1]:
                count += 1
    return count


matrix, rows, cols = read_matrix()
identical_count = identical_chr_count(matrix, rows, cols)
print(identical_count)
