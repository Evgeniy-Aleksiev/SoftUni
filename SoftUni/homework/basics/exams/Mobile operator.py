contract_duration = input()
contract_type = input()
addon_mobile_network = input()
months_payment = int(input())

contract_price = 0
if contract_duration == "one":
    if contract_type == "Small":
        contract_price = 9.98
    elif contract_type == "Middle":
        contract_price = 18.99
    elif contract_type == "Large":
        contract_price = 25.98
    elif contract_type == "ExtraLarge":
        contract_price = 35.99
elif contract_duration == "two":
    if contract_type == "Small":
        contract_price = 8.58
    elif contract_type == "Middle":
        contract_price = 17.09
    elif contract_type == "Large":
        contract_price = 23.59
    elif contract_type == "ExtraLarge":
        contract_price = 31.79

if addon_mobile_network == "yes":
    if contract_price <= 10:
        contract_price += 5.50
    elif contract_price <= 30:
        contract_price += 4.35
    else:
        contract_price += 3.85

final_price = contract_price * months_payment
if contract_duration == "two":
    final_price *= 0.9625

print(f"{final_price:.2f} lv.")