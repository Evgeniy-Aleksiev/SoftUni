def tags(param):
    def decorator(func):
        def wrapper(*args):
            res = f'<{param}>{func(*args)}</{param}>'
            return res
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
