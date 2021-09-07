command = input()
money_in_bank = 0

while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    else:
        money_in_bank += money
        print(f"Increase: {money:.2f}")
    command = input()
print(f"Total: {money_in_bank:.2f}")