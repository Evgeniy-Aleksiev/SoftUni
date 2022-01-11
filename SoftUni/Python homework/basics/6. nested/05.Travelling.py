destination = input()
while destination != "End":
    budget = float(input())
    total_saved_money = 0
    while total_saved_money < budget:
        saved_money = float(input())
        total_saved_money += saved_money
    print(f"Going to {destination}!")
    destination = input()