current_year = int(input())
while True:
    current_year += 1
    str_current_year = str(current_year)
    if len(str_current_year) == len(set(str_current_year)):
        print(str_current_year)
        break