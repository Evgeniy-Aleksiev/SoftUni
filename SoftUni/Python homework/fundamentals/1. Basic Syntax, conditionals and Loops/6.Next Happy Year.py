number = int(input())
next_year = number + 1
happy_year = ""
break_first_loop = False

while True:
    str_year = str(next_year)
    happy_year += str_year[0]
    for i in range(1, len(str_year)):
        for j in range(0, i):
            if str_year[i] == happy_year[j]:
                break_first_loop = True
                break
        if break_first_loop:
            break
        else:
            happy_year += str_year[i]
    if len(happy_year) == len(str_year):
        break
    happy_year = ""
    break_first_loop = False
    next_year += 1
print(happy_year)