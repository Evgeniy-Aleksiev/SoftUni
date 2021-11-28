# Test Three
def uppercase(func):
    def wrapper():
        result = func()

        uppercase_result = result.upper()
        return uppercase_result
    return wrapper


@uppercase
def say_hi():
    return 'hello evgeniy'


print(say_hi())
print(say_hi.__name__)


# Test two
# def print_message(message):
#     def message_sender():
#         print(message)
#     return message_sender()
#
#
# print_message('Hello world!')


# Test One
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi()
#
#
# hello = hello_function()
# print(hello)