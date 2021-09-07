party_size = int(input())
days = int(input())

coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        party_size -= 2
    if current_day % 15 == 0:
        party_size += 5
    coins += 50 - (party_size * 2)
    if current_day % 3 == 0:
        coins -= party_size * 3
    if current_day % 5 == 0:
        coins += party_size * 20
        if current_day % 3 == 0:
            coins -= party_size * 2
coins_each = int(coins / party_size)
print(f"{party_size} companions received {coins_each} coins each.")