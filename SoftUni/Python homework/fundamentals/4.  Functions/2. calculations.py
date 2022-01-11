def calculations(command, number_1, number_2):
    if command == 'multiply':
        return number_1 * number_2
    elif command == 'divide':
        return number_1 // number_2
    elif command == 'add':
        return number_1 + number_2
    elif command == 'subtract':
        return number_1 - number_2


operation = input()
num_1 = int(input())
num_2 = int(input())
print(calculations(operation, num_1, num_2))