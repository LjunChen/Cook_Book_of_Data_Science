import time
def time_cal(func):  
    def wrapper(*args):
        time1=time.time()
        result = func(*args)
        time2=time.time()
        print(f'The whole time is {time2-time1}')
        return result
    return wrapper


