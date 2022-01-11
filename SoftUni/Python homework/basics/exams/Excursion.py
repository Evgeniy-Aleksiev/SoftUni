number_of_people = int(input())
number_of_nights = int(input())
transport_cards_number = int(input())
museum_tickets_number = int(input())

nights = number_of_nights * 20
transport_cards = transport_cards_number * 1.60
museum_tickets = museum_tickets_number * 6
total_price_per_person = nights + transport_cards + museum_tickets
total_group_price = total_price_per_person * number_of_people
other_costs = total_group_price * 0.25 + total_group_price
print(f"{other_costs:.2f}")