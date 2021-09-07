more_than_20kg = float(input())
kg_of_the_bag = float(input())
days_before_the_trip = int(input())
number_bags = int(input())
price_of_the_bag = 0

if kg_of_the_bag < 10:
    price_of_the_bag += more_than_20kg * 0.20
elif kg_of_the_bag <= 20:
    price_of_the_bag += more_than_20kg / 2
else:
    price_of_the_bag = more_than_20kg

if days_before_the_trip < 7:
    price_of_the_bag += price_of_the_bag * 0.40
elif days_before_the_trip <= 30:
    price_of_the_bag += price_of_the_bag * 0.15
else:
    price_of_the_bag += price_of_the_bag * 0.10

total_price = price_of_the_bag * number_bags
print(f"The total price of bags is: {total_price:.2f} lv. ")
