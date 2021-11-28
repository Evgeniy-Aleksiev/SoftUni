class func_logger:

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_str = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_str + '\n')
        return self.func(*args)


@func_logger
def say_hi(name):
    print(f'Hi, {name}')


@func_logger
def say_bye(name):
    print(f'Bye, {name}')


say_hi('Pesho')
say_bye('Pesho')