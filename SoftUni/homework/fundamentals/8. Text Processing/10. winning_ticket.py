tickets = [t.strip() for t in input().split(", ") if not t.isspace()]

winning_symbol_at = "@" * 6
winning_symbol_hash = "#" * 6
winning_symbol_dollar = "$" * 6
winning_symbol_circumflex = "^" * 6

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    left_side = ticket[:10]
    right_side = ticket[10:]

    winning_symbol = ""

    if winning_symbol_at in left_side and winning_symbol_at in right_side:
        winning_symbol += "@"
    elif winning_symbol_hash in left_side and winning_symbol_hash in right_side:
        winning_symbol += "#"
    elif winning_symbol_dollar in left_side and winning_symbol_dollar in right_side:
        winning_symbol += "$"
    elif winning_symbol_circumflex in left_side and winning_symbol_circumflex in right_side:
        winning_symbol += "^"
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    left_side_symbol = left_side.count(winning_symbol)
    right_side_symbol = right_side.count(winning_symbol)
    minimum_symbols = min(left_side_symbol, right_side_symbol)

    if minimum_symbols < 10:
        print(f'ticket "{ticket}" - {minimum_symbols}{winning_symbol}')
    else:
        print(f'ticket "{ticket}" - {minimum_symbols}{winning_symbol} Jackpot!')


