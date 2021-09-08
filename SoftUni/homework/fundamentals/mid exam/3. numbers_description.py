numbers = [int(num) for num in input().split()]

average_number = sum(numbers) / len(numbers)
above_average = [num for num in numbers if num > average_number]
above_average.sort(reverse=True)
if len(above_average) == 0:
    print("No")
else:
    top_five = above_average[:5]
    str_top_five = [str(i) for i in top_five]
    print(" ".join(str_top_five))


