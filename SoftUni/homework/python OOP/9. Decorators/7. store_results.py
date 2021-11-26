class store_results:
    _logfile = 'results.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_str = f"Function {self.func.__name__} was add called. Result: {self.func(*args)}"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_str + '\n')


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
