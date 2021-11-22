def squares(n):
    # Variant one
    # for x in range(1, n+1):
    #     yield x**2

    # Variant two
    num = 1
    while num <= n:
        yield num**2
        num += 1


print(list(squares(5)))