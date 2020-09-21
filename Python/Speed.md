# Python运行加速技巧

Python 是一种解释型语言，相比于C/JAVA 之类静态语言，其运行速度显得很慢。 这里我们讨论一些Python加速的技巧。当然，一种加速的技巧是采用更好的算法，这个不在这个套路的范围之内。根据我目前的理解，主要有3类优化的方法.
* 优化Python本身的代码
* 利用Numba等包来加速一些计算
* 利用C等静态语言来写一些核心的计算

第一种方法，是最容易使用的，因为只涉及到一些语言的改写. 第二种方法, 确实也有效果，而且使用起来非常简单，就是加一个装饰器，但是有些时候，效果未必很好。 第三种方法，其实算是最有效率的方法，当然也最麻烦，需要掌握C的一些知识，不过利用cython可以将我们的Python类型的代码转化为C语言的代码(当然这需要一些技巧).


优化是需要牺牲点一些东西的，最起码会牺牲掉一些可读性。因此，只会在运行速度出现制约的时候，优化才会具有意义。而且我们需要优化的并不是全局代码，而是那些计算量很大的代码。

## 优化Python 代码
1. 尽量避免全局变量
相对来说，查找全局变量比查找局部变量，要慢，因此，我们尽量只使用局部变量，将所有的代码放在函数内，最终的执行代码也可以放在一个叫`main`的函数里面.
这应该成为一种习惯，尽量不要使用全局变量.

2. 尽量避免使用`.`
这一点其实是会降低Python代码的可读性的，因此酌情使用. Python每次使用`.`时，会触发特定的方法，如`__getattribute__(), _getattr()`,会带来额外的成本，特别是在一些循环中反复使用`.`方法的时候，会带来很大的成本.
考虑这一原则，我们在代码中导入模块的时候，使用`from math import sqrt`比使用`import math`然后调用`math.sqrt`要好. 在一个循环中，如果我们要反复地向一个list里面append数据时，我们可以使用`x=[], x_append=x.append, x_append(item)`会比常规的使用`x.append(item)`要快。
当然，这会让我们的代码不够Pythonic,降低了一些可读性，因此，在我看来，除非是真的在代码中反复调用`.`(如一个超大的循环中)，其他的时候还是使用`.`会比较好.

3. 用`for`循环来代替`while`循环
Python的`for`循环是比`while`循环要快的，因此能用`for`循环的可以尽量用`for`循环，当然，有些语句是更适合用`while`循环写的，没有必要过于强求.

4. 尽量用Python的内置方法
很多的内置方法都是经过专门的优化的，因此使用这些内置方法比你专门用python去实现的这些方法的效率要高很多.
* 实现对一个list的求和, `sum()`函数肯定是比你用循环实现的结果要好的. 
* 字符串拼接的`.join`方法，比循环加起来要好很多
* 使用`map`函数来取代循环，python的循环是非常慢的，因此能不用循环的尽量不要用循环.
* 在计算的时候，多用`numpy`包，numpy的核心几乎全部使用`C`语言写的，其速度非常快，几乎和用完全的`C`写出来的差不多，因此尽量使用`numpy`来进行计算.

## Numba
numba加速的主要原理是将python的代码转化为机器码去执行. 我们知道python这样的解释型语言是不产生机器码的，而是产生一些中间码去被一些解释器执行的，因此导致效率比较低. 

Numba的优势:
* 简单，往往我们只要一行代码的装饰器就可以了
* 对循环有奇效（很多时候最限制我们速度的就是循环了）
* 支持调用GPU

我们下面看一个numba使用的例子
```python
##使用numba装饰器
from numpy import jit
nb.jit()
def nb_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum

# 没用numba加速的求和函数
def py_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum
```
在数组`a`的长度很小的时候，numba的效果不是很明显，但是当`a`的长度很大的时候,numba的效果就非常明显了. 当然上述的例子，我们完全可以用numpy来写. 能用numpy的函数的，肯定还是用numpy的函数比较简单. 但是，有些时候，我们的循环没办法用numpy来改写的时候，numba就有效果了.

numba也可以和numpy一样,让一个普通函数变成一个`矢量函数`. 比如我们要对一个大型数据里面的每个元素求`sqrt`, 由于存在`np.sqrt`倒也不用使用numba,但是如果碰到一些numpy没有的函数的时候，我们就可以使用numba了,其具体调用方法为
```python
from math import sqrt
from numba import vectorize
@vectorize()
def nb_sqrt(a):
    return sqrt(a)
```
如果我们想要使用并行计算，直接在`jit,vectorize`的装饰器里面使用参数`parallel=True`就可以使用并行了. 另外，numba支持GPU,暂时没写过什么GPU程序，用过的都是tensorflow和pytorch去调用gpu的，暂时用不到.
总的来说，个人觉得在需要使用numba的场合，大部分都可以被numpy所替代，只有少量的numpy无法使用的情况，numba可以使用.

## 利用 C/Cython
我们可以考虑用C和Python的混合编程来实现加速的目的，主要结构用Python来写，而核心计算使用C语言来实现. 不过相对而言C的入门门槛比较高，直接写C语言比较难.

### Cython
Cython可以将我们写的Python代码直接转化为C语言的代码，而后调用C语言的编译器来编译C代码. 因此想要使用Cython的话，需要有C的编译器. win10里面需要安装Visual Studio. 但是有些时候还是有些莫名其妙的bug. 最好的还是在Linux环境里面使用.

原生的Python代码可以通过Cython进行加速，但是效果不是特别明显。这里值得注意的是Python的数据类型都是动态的，因此解释器要花很大的时间来推断这个数据类型。而C的数据类型是静态的，所以很快，我们在Cython中，可以用一些关键字来明确变量的数据类型，这样使用Cython的效果才是最好的.

我们考虑一个例子，计算斐波那契数据

```python
def c_py_fib(n):
    a,b=0,1
    for i in range(n):
        a,b=a+b,a
    return a

def c_fib(int n):
    cdef double a=0.0
    cdef double b=1.0
    cdef int i
    for i in range(n):
        a,b=a+b,a
    return a
```


然后我们把这个文件保存为 `fib.pyx`, 注意后缀是 `.pyx`

然后我们创建一个 `setup.py` 文件, 内容如下

```python
from setuptools import  setup
from Cython.Build import cythonize
setup(ext_modules=cythonize('fib.pyx'))
```

接着我们可以打开终端(或者cmd) 执行

```
python setup.py build_ext --inplace
```

在我的电脑里面产生了一个 ` fib.cp37-win_amd64.so`的文件（在win10里面，我试了一下好像是 fib.cp37-win_amd64.pyd），还有一个fib.c文件，build文件夹（fib.c是产生的c的源文件，这两个应该都是没用的，我试过删掉这两个东西，不影响结果）.

然后我们通过python去调用这个函数

```python
import  time
from fib import c_py_fib
def main():
    n=100
    start=time.time()
    result=c_py_fib(n)
    end=time.time()
    print('结果为{}'.format(result))
    print('时间为{}'.format(end-start))

    from fib import c_fib
    start=time.time()
    result=c_fib(n)
    end=time.time()
    print('结果为{}'.format(result))
    print('时间为{}'.format(end-start))
main()
```
第二种方法比第一种方法快5倍左右，当然这些都比原生的python快很多.

> 这里`from fib import fib` 调用的是` fib.cp37-win_amd64.so`，这里以fib开头的还有`fib.pyx`，然后python的 import 只会导入`.py`/`.pyc`/`.pyo`/`.pyd`/`.so`文件中的内容，不会进`.pyx`文件中进行寻找。


### 直接编译C的代码
我们可以写一段C语言的代码，保存为`clib.c`用来计算斐波那契数列
```c
#include "stdio.h"
int fib(int n){
    int a=0;
    int b=1;
    int i;
    int tmp;
    for(i=0;i<n;i++){
        tmp = a;
        a = a + b;
        b = tmp;
    }
    return a;
}
```
然后命令行`gcc -shared -fPIC clib.c -o clib.so`来编译形成`clib.so`文件. 现在我们就可以在python中调用这个数学函数了
```python
import time
import ctypes
def main():
    start=time.time()
    clib = ctypes.cdll.Loadlibrary("clib.so")
    result = clib.fib(30)
    end=time.time()
    print('结果为{}'.format(result))
    print('时间为{}'.format(end-start))
main()
```
但是这样的调用有时候是有问题的，在传入的参数是整数的时候，一般还好，其他类型的数字就不行了，记住C是静态类型，不会像Python那那样
去识别数据类型，因此最好的调用是
```python
result = clib.fib(ctypes.c_int(30))
```
其他参数的传入同理.
