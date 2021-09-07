easter_bread = int(input())
eggs = int(input())
kg_cookies = int(input())

eggs_paint = eggs * 12 * 0.15
total_price = easter_bread * 3.20 + eggs * 4.35 + kg_cookies * 5.40 + eggs_paint
print(f"{total_price:.2f}")
