number_guest = int(input())
envelope_per_guest = float(input())
budget = float(input())

if 10 <= number_guest <= 15:
    envelope_per_guest *= 0.85
elif 15 < number_guest <= 20:
    envelope_per_guest *= 0.80
elif number_guest > 20:
    envelope_per_guest *= 0.75

cake_price = budget * 0.10
total_price = envelope_per_guest * number_guest + cake_price

difference = abs(total_price - budget)
if total_price <= budget:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")