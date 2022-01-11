def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def print_result(lots):
    if lots:
        print(*[car_num for car_num in parking_lot], sep='\n')
    else:
        print("Parking Lot is Empty")


lines = input_to_list(int(input()))
parking_lot = set()

for line in lines:
    command, register_number = line.split(', ')

    if command == "IN":
        parking_lot.add(register_number)
    elif command == "OUT":
        parking_lot.remove(register_number)

print_result(parking_lot)