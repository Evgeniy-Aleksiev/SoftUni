for row in range(8):
    for col in range(9):
        if (row == 0 and 2 <= col < 7) or (row == 1 and 1 <= col < 8) or\
                ((row == 2 or row == 3) and col != 2 and col != 3 and col != 5 and col != 6) or (row == 4 and col != 4) or\
                (row == 5 and (col == 1 or col == 2 or col == 6 or col == 7)) or ((row == 6 or row == 7) and 2 <= col < 7):
            print("F", end="")
        else:
            print(end=" ")
    print()