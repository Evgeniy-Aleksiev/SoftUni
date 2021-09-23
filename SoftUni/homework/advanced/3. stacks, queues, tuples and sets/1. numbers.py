first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])


for _ in range(int(input())):
    cmd = input()

    if cmd.startswith('Add'):
        _, position, *numbers = cmd.split()

        if position == "First":
            [first_sequence.add(int(number)) for number in numbers]

        elif position == "Second":
            [second_sequence.add(int(number)) for number in numbers]

    elif cmd.startswith('Remove'):
        _, position, *numbers = cmd.split()
        current_set = set([int(x) for x in numbers])

        if position == "First":
            first_sequence = first_sequence.difference(current_set)
        elif position == "Second":
            second_sequence = second_sequence.difference(current_set)

    elif cmd.startswith('Check'):
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(', '.join(map(str, sorted(first_sequence))))
print(', '.join(map(str, sorted(second_sequence))))
