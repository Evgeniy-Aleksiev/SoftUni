number = float(input())
unit = input()
result_unit = input()
sum = 0
if unit == "m":
    if result_unit == "mm":
        sum = number * 1000
    elif result_unit == "cm":
        sum = number * 100
elif unit == "cm":
    if result_unit== "m":
        sum = number / 100
    elif result_unit == "mm":
        sum = number * 10
elif unit == "mm":
    if result_unit == "m":
        sum = number / 1000
    elif result_unit == "cm":
        sum = number / 10

print(f"{sum:.3f}")