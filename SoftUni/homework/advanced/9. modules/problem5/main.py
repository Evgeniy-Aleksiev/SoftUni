from helper import generate_sequence, find_number

data = input()
sequence = []

while not data == 'Stop':
    cmd = data.split()
    command = cmd[0]
    number = int(cmd[-1])

    if command == 'Create':
        sequence = generate_sequence(number)
        print(' '.join(map(str, sequence)))

    elif command == 'Locate':
        result = find_number(number, sequence)
        print(f"The number - {number} is at index {result}" if isinstance(result, int) else result)

    data = input()