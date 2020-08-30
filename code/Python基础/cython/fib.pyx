def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    import time
    start=time.time()
    result=fib(40)
    end=time.time()
    print('结果为{}'.format(result))
    print('时间为{}'.format(end-start))
    