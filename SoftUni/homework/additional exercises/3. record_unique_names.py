def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


names = set(input_to_list(int(input())))
print(*[name for name in names], sep='\n')
