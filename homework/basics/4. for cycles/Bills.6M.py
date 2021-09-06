months = int(input())
electricity_price = 0

for electricity in range(months):
    electricity = float(input())
    electricity_price += electricity
    water_price = months * 20
    internet_price = months * 15

other = electricity_price + water_price + internet_price
other_price = other * 0.20 + other
average = (electricity_price + water_price + internet_price + other_price) / months

print(f"Electricity: {electricity_price:.2f} lv")
print(f"Water: {water_price:.2f} lv")
print(f"Internet: {internet_price:.2f} lv")
print(f"Other: {other_price:.2f} lv")
print(f"Average: {average:.2f} lv")