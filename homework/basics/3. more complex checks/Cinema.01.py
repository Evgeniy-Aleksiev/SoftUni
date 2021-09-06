projection_type = input()
number_rows = int(input())
number_columns = int(input())
income = 0
capacity = number_rows * number_columns
if projection_type == "Premiere":
    income = capacity * 12.00
elif projection_type == "Normal":
    income = capacity * 7.50
elif projection_type == "Discount":
    income = capacity * 5.00

print(f"{income:.2f} leva")
