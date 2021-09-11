for row in range(5):
    for col in range(6):
        if (row != 3 and row != 4 and col == 2) or (row != 3 and row != 4 and col == 3) or row == 3 or row == 4:
            print("@", end="")
        else:
            print(end=" ")
    print()
