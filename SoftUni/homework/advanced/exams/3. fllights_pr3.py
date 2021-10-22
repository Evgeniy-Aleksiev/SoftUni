def flights(*args):
    flight_destination = {}
    current_destination = ''

    for el in args:
        if el == 'Finish':
            break

        if isinstance(el, int):
            flight_destination[current_destination] += el
            current_destination = ''
            continue
        if el not in flight_destination:
            flight_destination[el] = 0
        current_destination = el

    return flight_destination


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
