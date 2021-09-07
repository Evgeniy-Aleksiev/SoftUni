budget = float(input())
command = input()
the_budget_not_enough = False

while command != "ACTION":
    actor_name = command
    if len(actor_name) > 15:
        salary = budget * 0.20
    else:
        salary = float(input())
    budget -= salary
    if budget < 0:
        the_budget_not_enough = True
        break
    command = input()
if the_budget_not_enough:
    print(f"We need {abs(budget):.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")