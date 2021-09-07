flour = int(input())
room = int(input())

for f in range(flour, 0, -1):
    for r in range(room):
        if f == flour:
            print(f"L{f}{r}", end=" ")
        else:
            if f % 2 == 0:
                print(f"O{f}{r}", end=" ")
            else:
                print(f"A{f}{r}", end=" ")
    print()