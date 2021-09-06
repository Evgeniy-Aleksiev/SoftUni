expected_amount = int(input())
cash_paid = 0
card_paid = 0
number_cash_paid = 0
number_card_paid = 0
total_collect = 0
funds_raised = False
command = input()
current_alternate = 0

while command != "End":
    product_price = int(command)
    current_alternate += 1
    if current_alternate % 2 == 1:  # плащане в брой
        if product_price > 100:
            print("Error in transaction!")
        else:
            cash_paid += product_price
            number_cash_paid += 1
            total_collect += product_price
            print("Product sold!")
    else:  # плащане с карта
        if product_price < 10:
            print("Error in transaction!")
        else:
            card_paid += product_price
            number_card_paid += 1
            total_collect += product_price
            print("Product sold!")
    if total_collect >= expected_amount:
        funds_raised = True
        break
    command = input()

average_cash_paid = cash_paid / number_cash_paid
average_card_paid = card_paid / number_card_paid
if funds_raised:
    print(f"Average CS: {average_cash_paid:.2f}")
    print(f"Average CC: {average_card_paid:.2f}")
elif command == "End":
    print("Failed to collect required money for charity.")