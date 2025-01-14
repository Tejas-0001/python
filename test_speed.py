import time

def speed_calc_decorator(function):
    def test():
        current_time = time.time()
        function()
        print(f"{function.__name__} : {time.time()-current_time}")
    return test

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()