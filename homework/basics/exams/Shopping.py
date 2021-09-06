budget = float(input())
gpu_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

gpu_price = gpu_amount * 250
cpu_price = (gpu_price * 0.35) * cpu_amount
ram_price = (gpu_price * 0.10) * ram_amount
total_price = gpu_price + cpu_price + ram_price
if gpu_amount > cpu_amount:
    total_price *= 0.85

difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")