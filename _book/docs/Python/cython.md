## Cython



我们知道，相比于底层语言(C,Java,Go等), Python 的计算速度是很慢的，因此我们可以考虑将部分Python的代码编译成C语言代码，通过C语言的运行效率来加速我们的计算。

在这方面，我们有两种选择，一是核心代码直接用C来写，但是这就需要你对C有足够的了解。另一种方式是直接通过写Python代码，然后通过一些手段转化成C的代码再进行编译（非常简单，但是可能灵活性没有第一种方法好）。

Cython 库可以很好的帮我们把Python的代码编译为C语言的代码。

安装方式

```
pip install cython
```

> cpython 在Linux里面work well. 在windows里面安装的时候，需要安装Visual Studio Build Tools (或者直接安装Visual Studio也可以)，不过这两个都很占空间。



我们考虑一个例子，用递归算法实现对斐波那契数列的计算

```python
def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)
```

> P.S. 这只是一个例子，我们当然有很多方法来优化这个算法，目前这个对斐波那契数列的计算有太多的重复计算，具体见递归算法部分。

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

在我的电脑里面产生了一个 ` fib.cp37-win_amd64.so`的文件（在win10里面，我试了一下好像是 fib.cp37-win_amd64.pyd），还有一个fib.c文件，build文件夹（这两个应该都是没用的，我试过删掉这两个东西，不影响结果）.

然后我们通过python去调用这个函数

```python
import  time
from fib import fib
start=time.time()
result=fib(40)
end=time.time()
print('结果为{}'.format(result))
print('时间为{}'.format(end-start))
```

> 这里`from fib import fib` 调用的是` fib.cp37-win_amd64.so`，这里以fib开头的还有`fib.pyx`，然后python的 import 只会导入`.py`/`.pyc`/`.pyo`/`.pyd`/`.so`文件中的内容，不会进`.pyx`文件中进行寻找。

可以比较一下python的源生调用的时间和利用c编译的函数的时间，一个需要6s左右，一个需要30s左右，速度提高了5倍左右。

> P.S. 这个技巧在某种程度上来说是很有用的。不过有些做的很好的python的第三方库,比如numpy,其本身的很多核心代码就是用c写的，所以我们也不需要做这一步了。

