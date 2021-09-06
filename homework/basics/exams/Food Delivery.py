chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

total_menu_price = chicken_menu * 10.35 + fish_menu * 12.40 + vegan_menu * 8.15
desert = total_menu_price * 0.20
total_price = total_menu_price + desert + 2.50
print(f"Total: {total_price:.2f}")