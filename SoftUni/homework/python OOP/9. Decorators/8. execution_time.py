import time


def exec_time(func):
    def wrapper(*args):
        start_timer = time.time()
        func(*args)
        end_timer = time.time()
        return end_timer - start_timer
    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())
