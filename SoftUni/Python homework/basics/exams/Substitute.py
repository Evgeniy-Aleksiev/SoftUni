k = int(input())    # Първо число от първия номер
l = int(input())    # Второ число от първия номер
m = int(input())    # Първо число от втория номер
n = int(input())    # Втория число от втория номер

count = 0
six_players_swap = False
for first_number_k in range(k, 8 +1):
    if first_number_k % 2 == 0:
        even_first_number_k = first_number_k
    else:
        continue
    for second_number_l in range(9, l -1, -1):
        if second_number_l % 2 == 1:
            odd_second_number_l = second_number_l
        else:
            continue
        for first_number_m in range(m, 8 +1):
            if first_number_m % 2 == 0:
                even_first_number_m = first_number_m
            else:
                continue
            for second_number_n in range(9, n -1, -1):
                if second_number_n % 2 == 1:
                    odd_second_number_n = second_number_n
                else:
                    continue

                if first_number_k == first_number_m and second_number_l == second_number_n:
                    print("Cannot change the same player.")
                else:
                    print(f"{even_first_number_k}{odd_second_number_l} - {even_first_number_m}{odd_second_number_n}")
                    count += 1
                if count >= 6:
                    six_players_swap = True
                    break
            if six_players_swap:
                break
        if six_players_swap:
            break
    if six_players_swap:
        break
