username = input().split(", ")
its_valid = False

for el in username:
    if 3 <= len(el) <= 16:
        its_valid = True
    else:
        its_valid = False
        continue
    for ch in el:
        if ch.isdigit() or ch.isalpha() or ch == "-" or ch == "_":
            its_valid = True
        else:
            its_valid = False
            break
    if its_valid:
        print(el)
