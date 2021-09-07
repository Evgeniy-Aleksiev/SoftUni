def sequence(number: int):
    current_number = []
    for num in range(number):
        if num == 0:
            current_number.append(1)
        else:
            sum_of_numbers = sum(current_number[-3:])
            current_number.append(sum_of_numbers)

    nums_to_str = [str(nums) for nums in current_number]

    return nums_to_str


n = int(input())

print(" ".join(sequence(n)))
