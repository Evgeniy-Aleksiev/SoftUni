def sequence(*args):
    negative_sum = 0
    positive_sum = 0

    for num in args:
        if num < 0:
            negative_sum += num
            continue

        positive_sum += num

    return negative_sum, positive_sum


numbers = [int(x) for x in input().split()]
negative, positive = sequence(*numbers)
print(f'{negative}\n{positive}')

if abs(negative) > positive:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

