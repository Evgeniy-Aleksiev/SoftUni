def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


sum_first_n = sum(first_n(5))
print(sum_first_n)


def second_n(n):
    num = 0
    while num < n:
        yield num
        num += 1


for el in second_n(5):
    print(el)
