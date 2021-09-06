flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
may = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 0.10 + flour_price
may_price = sugar_price * 0.20
total_price = flour_price * flour_kg + sugar_price * sugar_kg + eggs_price * eggs + may_price * may
print(f"{total_price:.2f}")