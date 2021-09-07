list_of_integers = input().split()
count_of_numbers_to_remove = int(input())

int_list = []

for i in range(len(list_of_integers)):
    int_list.append(int(list_of_integers[i]))

for i in range(count_of_numbers_to_remove):
    min_size = min(int_list)
    int_list.remove(min_size)

for i in range(len(int_list)):
    int_list[i] = str(int_list[i])

print(", ".join(int_list))