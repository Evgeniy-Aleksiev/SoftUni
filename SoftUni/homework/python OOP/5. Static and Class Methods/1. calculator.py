class Calculator:
    @staticmethod
    def add(*args):
        result = 0
        for x in args:
            result += x
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(first_num, *args):
        result = first_num
        for x in args:
            result /= x
        return result

    @staticmethod
    def subtract(first_num, *args):
        result = first_num
        for x in args:
            result -= x
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

