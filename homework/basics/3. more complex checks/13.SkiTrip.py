days = int(input())
room = input()
final_assessment = input()
nights = days - 1
discount = 0
room_for_one_person = 18 * nights
apartment_price = 25 * nights
president_apartment = 35 * nights

if room == "apartment":
    if days < 10:
        discount = apartment_price * 0.70
    elif 10 <= days <= 15:
        discount = apartment_price * 0.65
    elif days > 15:
        discount = apartment_price * 0.50
elif room == "president apartment":
    if days < 10:
        discount = president_apartment * 0.90
    elif 10 <= days <= 15:
        discount = president_apartment * 0.85
    elif days > 15:
        discount = president_apartment * 0.80

if final_assessment == "positive":
    if room == "room for one person":
        discount = room_for_one_person * 0.25 + room_for_one_person
    elif room == "apartment":
        discount = discount * 0.25 + discount
    elif room == "president apartment":
        discount = discount * 0.25 + discount
elif final_assessment == "negative":
    if room == "room for one person":
        discount = abs(room_for_one_person * 0.10 - room_for_one_person)
    elif room == "apartment":
        discount = abs(discount * 0.10 - discount)
    elif room == "president apartment":
        discount = abs(discount * 0.10 - discount)

print(f"{discount:.2f}")