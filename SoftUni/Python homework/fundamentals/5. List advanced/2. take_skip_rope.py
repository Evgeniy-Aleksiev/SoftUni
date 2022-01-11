text = input()

number_list = [int(x) for x in text if x.isdigit()]
non_number_list = [x for x in text if not x.isdigit()]

hidden_message = []

for index in range(len(number_list)):
    if index % 2 == 0:
        take_num = number_list[index]
        if not take_num == 0:
            take = non_number_list[:take_num]
            hidden_message.extend(take)
        for current_take in range(0, take_num):
            if non_number_list:
                non_number_list.pop(0)
            else:
                break

    elif not index % 2 == 0:
        skip_num = number_list[index]
        if not skip_num == 0:
            del non_number_list[:skip_num]

print("".join(hidden_message))
