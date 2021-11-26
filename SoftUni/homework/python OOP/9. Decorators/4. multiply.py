def multiply(n):
    def decorator(func):
        def wrapper(num):
            return func(num) * n
        return wrapper
    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))

