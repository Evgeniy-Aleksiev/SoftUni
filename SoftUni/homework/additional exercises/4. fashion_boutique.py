clothes_in_the_box = [int(x) for x in input().split()]
rack_capacity = int(input())
current_box = 0
number_of_racks = 0

while clothes_in_the_box:
    piece_of_clothes = clothes_in_the_box.pop()

    if current_box + piece_of_clothes <= rack_capacity:
        current_box += piece_of_clothes
    else:
        number_of_racks += 1
        current_box = piece_of_clothes

    if len(clothes_in_the_box) == 0:
        number_of_racks += 1

print(number_of_racks)