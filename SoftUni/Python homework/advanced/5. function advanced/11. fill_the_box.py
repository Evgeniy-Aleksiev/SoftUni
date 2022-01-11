def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    no_more_space = False
    left_cubes = 0

    for cube in args:
        if cube == 'Finish':
            break

        if cube > box_size and not no_more_space:
            no_more_space = True
            left_cubes += cube - box_size
            box_size = 0
            continue

        if cube > box_size:
            left_cubes += cube
        else:
            box_size -= cube

    if box_size:
        return f"There is free space in the box. You could put {box_size} more cubes."
    return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
