def some_func(n):
    if n == 1:
        return 1
    return n * some_func(n - 1)


print(some_func(3))