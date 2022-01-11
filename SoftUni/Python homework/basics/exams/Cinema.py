hall_capacity = int(input())
command = input()
the_cinema_is_full = False
total_price = 0
total_people_entry = 0

while command != "Movie time!":
    people_entry = int(command)
    total_people_entry += people_entry
    ticket_price = 5 * people_entry
    if people_entry % 3 == 0:
        ticket_price -= 5
    if total_people_entry > hall_capacity:
        the_cinema_is_full = True
        break
    else:
        total_price += ticket_price
        command = input()

if command == "Movie time!":
    print(f"There are {hall_capacity - total_people_entry} seats left in the cinema.")
if the_cinema_is_full:
    print("The cinema is full.")
print(f"Cinema income - {total_price} lv.")