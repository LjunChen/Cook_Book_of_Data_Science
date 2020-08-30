# 利用Pysnooper进行Debug

不同的人debug的方法不是特别一样，有些人比较喜欢用一些成熟的debug 工具（断点调试之类的），也有人喜欢用print函数去打印一些关键信息（如变量的值，类型，形状等等），以此来判断代码出错的位置。

相比之下，断点调试是更加专业的debug工具，然而print方法可能更加简单（也很好用，并且不依赖于很强大的编辑器).

pysnooper实质上是print调试方法的一个替代品，我们用print方法debug的时候，需要细致的去写要print出哪些内容，而pysnooper只需要在我们感兴趣的函数上加个修饰器，我们就可以得到整个函数运行的整个log, 包括函数的哪一行在什么时间执行，变量的值的变化，等等。并且我们可以将整个日志轻松的输出到一个文件。

下面是pysnooper的一个例子

```python
import pysnooper
import numpy as np

@pysnooper.snoop('log.txt')
def multi_matmul(times):
    x=np.random.rand(2,2)
    w=np.random.rand(2,2)
    y=2
    for i in range(times):
        x=np.matmul(x,w)
        y=y*2
    return x

multi_matmul(40)

```

我们就用了一句代码来检测整个函数运行的过程中变量的值的变化，什么时间点运行了什么函数等等，并且我指定将log输出到log.txt文件。

