def fibonacci():
    fib_0 = 0
    fib_1 = 1

    yield fib_0
    yield fib_1

    while True:
        fib = fib_0 + fib_1
        fib_0, fib_1 = fib_1, fib
        yield fib


generator = fibonacci()
for i in range(1):
    print(next(generator))
