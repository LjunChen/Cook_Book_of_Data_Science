# Python的装饰器

装饰器本身上是一个Python函数，它可以让其他函数在**不需要变动任何代码的前提下**增加额外功能。比如我们想要给函数计时，加日志等，直接修改这些函数的源代码，有时候不够方便（比如我们只想计时，而函数的source code很复杂的时候），也任意出错，并且不够美观。

简单来讲，装饰器的作用就是给目前的函数添加额外的功能。

我们首先看一个简单的例子，假设我们目前有个求斐波那契数列的函数

```python
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
```

现在我们希望这个函数在运行的时候，可以打印出来整个代码的运行时间（P.S. 为了时间长点，选择了这个计算效率很差的算法来计算斐波那契数列）。

现在我们定义一个用来计算时间的装饰器函数

```python
import time
def functime(func):
    def wrapper(*args):
        t1 =  time.time()
        result = func(*args)
        t2 = time.time()
        print('The process time is {:.4} s'.format(t2-t1))
        return result
    return wrapper
```

这样处理还有几个好处。首先，我们将实现程序的主体功能和附属功能分离了，其次计算时间的函数可能会在很多个函数里面使用，这样可以使得我们的代码更加简单美观。

然后我们定义一个新的函数

```python
@functime
def fib2(n):
    result = fib(n)
    print('The {}th of fib series is {}'.format(n,result))
    
fib2(30)
```

这样就可以在运行核心函数 `fib`的同时计算时间。这里我们定义了一个 `fib2`是因为`fib`函数本身是个递归过程，如果直接把装饰器加在`fib`上的话，打印会很混乱。

另外，使用装饰器可以更好的处理日志信息

```python
from functools import wraps
 
def logit(func):
    def logging_info(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return logging_info
 
@logit
def myfunc(x):
   return x**2
 
 
result = myfunc(4)
print(result)
```









