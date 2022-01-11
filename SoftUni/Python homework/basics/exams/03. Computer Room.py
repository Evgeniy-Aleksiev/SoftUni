month = input()
hours_spent = int(input())
group_people = int(input())
time_of_the_day = input()

price_per_h = 0
if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price_per_h = 10.50
    elif time_of_the_day == "night":
        price_per_h = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_the_day == "day":
        price_per_h = 12.60
    elif time_of_the_day == "night":
        price_per_h = 10.20

if group_people >= 4:
    price_per_h *= 0.90
if hours_spent >= 5:
    price_per_h *= 0.50

total_price = price_per_h * group_people * hours_spent

print(f"Price per person for one hour: {price_per_h:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")