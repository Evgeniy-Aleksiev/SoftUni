def print_row(size, star_count):
    for empty_space in range(size - star_count):
        print(' ', end='')
    for star_row in range(1, star_count):
        print('*', end=' ')
    print('*')


size_of_rhombus = int(input())
for rhombus_top_side in range(1, size_of_rhombus):
    print_row(size_of_rhombus, rhombus_top_side)

for rhombus_down_side in range(size_of_rhombus, 0, -1):
    print_row(size_of_rhombus, rhombus_down_side)