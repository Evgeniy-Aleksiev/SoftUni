def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def is_unique(usernames):
    unique_usernames = set()
    for name in usernames:
        unique_usernames.add(name)
    return unique_usernames


names = input_to_list(int(input()))
unique = is_unique(names)

print(*[x for x in unique], sep='\n')
