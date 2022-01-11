str_of_int = input().split(", ")
count_of_beggars = int(input())

index = 0
sum_of_list = []

for beggar in range(1, count_of_beggars + 1):
    beggar_takes = 0

    for current_index in range(index, len(str_of_int), count_of_beggars):
        beggar_takes += int(str_of_int[current_index])

    index += 1
    sum_of_list.append(beggar_takes)

print(sum_of_list)
