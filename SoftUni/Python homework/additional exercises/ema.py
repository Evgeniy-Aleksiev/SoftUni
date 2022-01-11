# ако е 0,1, 7, 8, 16, 17 19, 20, 25, 26 са цели колони

for row in range(8):
    for col in range(27):
        if (col == 0 or col == 1 or col == 7 or col == 8 or col == 16 or col == 17 or col == 19 or col == 20 or col == 25 or col == 26) or\
                (col == 2 and row != 2 and row != 5) or (col == 3 and row != 2 and row != 5) or\
                (col == 4 and row != 2 and row != 5) or (col == 5 and row != 2 and row != 5) or\
                (row == 0 and (col == 9 or col == 15)) or (row == 1 and (col == 9 or col == 10 or col == 14 or col == 15)) or\
                (row == 2 and (col == 10 or col == 11 or col == 13 or col == 14)) or (row == 3 and (col == 11 or col == 12 or col == 13)) or\
                (row == 4 and col == 12) or ((row == 0 or row == 1 or row == 4) and 21 <= col < 25):
            print("@", end="")
        else:
            print(end=" ")
    print()