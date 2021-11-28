def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
                print(args)
        return wrapper
    return decorator


@repeat(5)
def say_hi(*args):
    print('Hello')


say_hi(1, 2, 3)
