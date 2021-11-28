def admin_access(ref_func):
    def wrapper(user_obj):
        if user_obj['is_admin']:
            return ref_func(user_obj)
        raise PermissionError("Only admins can access it")

    return wrapper


user = {'name': 'Test', 'is_admin': True}
user_not_admin = {'name': 'Testov', 'is_admin': False}


@admin_access
def read_book_content(user):
    print(f'{user["name"]} reads the book content')


def read_product_content(user):
    print(f"{user['name']} reads the book content")


read_book_content(user)


print('\n---------\n')


def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase
def speak():
    return 'hello i am speaking'


@uppercase
def speak_bulgarian():
    return 'Dobre'


print(speak())

print('\n---------\n')


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(5)
def say_hi():
    print('Hello')

say_hi()