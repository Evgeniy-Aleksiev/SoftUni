def is_inside(r, c):
    return 0 <= r < 6 and 0 <= c < 6

def prize(points):
    if points < 100:
        return f"Sorry! You need {100 - points} points more to win a prize."
    if points < 200:
        return f"Good job! You scored {points} points, and you've won Football."
    if points < 300:
        return f"Good job! You scored {points} points, and you've won Teddy Bear."
    if points >= 300:
        return f"Good job! You scored {points} points, and you've won Lego Construction Set."


def sum_of_column(board, r, c):
    column_sum = 0
    for row in range(6):
        if board[row][c] == 'B':
            continue
        column_sum += int(board[row][c])

    return column_sum


def play(board):
    throws = 3
    hitted_buckets = []
    total_points = 0

    while throws:
        row, col = input()[1:-1].split(', ')
        row = int(row)
        col = int(col)
        throws -= 1

        if is_inside(row, col):
            if board[row][col] == 'B' and [row, col] not in hitted_buckets:
                hitted_buckets.append([row, col])
                total_points += sum_of_column(board, row, col)
    return total_points


board = [input().split() for x in range(6)]
total_points = play(board)
print(prize(total_points))