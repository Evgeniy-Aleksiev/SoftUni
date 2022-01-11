def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def is_vip(guest):
    return guest[0].isdigit()


def sorted_by_codes(guests):
    vip_guests = []
    regular_guests = []

    for guest in guests:
        if is_vip(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)

    return sorted(vip_guests), sorted(regular_guests)


def print_results(guests, length):
    (vip_guests, regular_guests) = sorted_by_codes(guests)

    print(length)
    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


reservation_codes = input_to_list(int(input()))
guests_arrived = []

command = input()

while not command == "END":
    guests_arrived.append(command)

    command = input()

guest_not_arrived = set(reservation_codes).difference(guests_arrived)
number_guest_not_arrived = len(guest_not_arrived)

print_results(guest_not_arrived, number_guest_not_arrived)
