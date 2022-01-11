coins = float(input())
coins = int(coins * 100)
coins_sum = 0
coins_sum += coins // 200
coins %= 200
coins_sum += coins // 100
coins %= 100
coins_sum += coins // 50
coins %= 50
coins_sum += coins // 20
coins %= 20
coins_sum += coins // 10
coins %= 10
coins_sum += coins // 5
coins %= 5
coins_sum += coins // 2
coins %= 2
if coins == 1:
    coins_sum += 1
print(coins_sum)
