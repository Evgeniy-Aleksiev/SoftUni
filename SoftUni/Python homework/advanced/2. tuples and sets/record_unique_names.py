def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def unique(data):
    unique_names = set()

    for name in data:
        unique_names.add(name)

    print(*[name for name in unique_names], sep='\n')


names = input_to_list(int(input()))
unique(names)