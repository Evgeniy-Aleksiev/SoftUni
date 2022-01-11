def even_parameters(func):
    def wrapper(*args):
        res = any([x for x in args if not isinstance(x, int)])
        if not res:
            x = [x for x in args if x % 2 == 0]
            if len(x) == len(args):
                return func(*args)

        return 'Please use only even numbers!'
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

