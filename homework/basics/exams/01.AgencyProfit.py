agency_name = input()
adult_ticket = int(input())
kid_ticket = int(input())
price_adult_ticket = float(input())
service_fee = float(input())

price_kid_ticket = price_adult_ticket * 0.30
adult_ticket_with_fee = price_adult_ticket + service_fee
kid_ticket_with_fee = price_kid_ticket + service_fee
total_price = adult_ticket * adult_ticket_with_fee + kid_ticket * kid_ticket_with_fee
profit = total_price * 0.20

print(f"The profit of your agency from {agency_name} tickets is {profit:.2f} lv.")