width = int(input())
length = int(input())
cake_size = width * length
total_cakes = 0
command = input()
finish_the_cake = False

while command != "STOP":
    piece_of_cake = int(command)
    total_cakes += piece_of_cake
    if cake_size < total_cakes:
        finish_the_cake = True
        break
    command = input()

piece_cake_need = abs(total_cakes - cake_size)
if finish_the_cake:
    print(f"No more cake left! You need {piece_cake_need} pieces more.")
else:
    print(f"{piece_cake_need} pieces are left." )
