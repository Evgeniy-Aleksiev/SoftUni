town = input()
type_packet = input()
vip = input()
days = int(input())
invalid = False

price = 0
if town == "Bansko" or town == "Borovets":
    if type_packet == "withEquipment":
        price += 100
        if vip == "yes":
            price *= 0.90
    elif type_packet == "noEquipment":
        price += 80
        if vip == "yes":
            price *= 0.95
elif town == "Varna" or town == "Burgas":
    if type_packet == "withBreakfast":
        price += 130
        if vip == "yes":
            price *= 0.88
    elif type_packet == "noBreakfast":
        price += 100
        if vip == "yes":
            price *= 0.93
else:
    invalid = True

if days >= 7:
    days -= 1
total_price = price * days

if days <= 1:
    print("Days must be positive number!")
elif invalid or (type_packet != "noEquipment" and type_packet != "withEquipment" and\
                 type_packet != "noBreakfast" and type_packet != "withBreakfast"):
    print("Invalid input!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")