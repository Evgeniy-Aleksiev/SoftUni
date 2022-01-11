class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


for _ in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative
