## Python与R的交互: rpy2模块

我们知道，R里面有大量的统计学家写的包（特别是针对很多特定的问题），这些时候，我们可能很想使用R语言来帮助我们完成一些特定的功能。这个时候我们就需要使用到Python和R的交互了（前提要在电脑里装好R，并且写进了环境变量）。

rpy2 模块可以直接用`pip`安装，但是使用的时候可能会出一些问题.

windows下 要将R写进环境变量

```
C:\Software\R\R-4.0.1\bin\x64\R.dll
C:\Software\R\R-4.0.1\bin\x64
```

要将这两个都写进环境才可以（略微有点奇怪），我在windows下碰到过的错误就是找不到这个`R.dll`，这个写进环境之后才可以。

Linux 下出现了一个错误 `Import Error: .../libreadline.so: undifined Symbol:PC`, 不太懂是什么意思，百度了一下的解释是`conda 内置readline包没有链接到ncurses库`， 解决办法是将 Linux的 `libreadline.so`复制到Anaconda里面 (后面那部分换成自己的anaconda的安装地址).

```
cp -p /lib/x86_64-linux-gnu/libreadline.so.6 ~/anaconda/lib/libreadline.so.6
```





模块rpy2.robjects 是rpy2对R的一个高级封装，使用rpy2的大多数情况，都只需要和这个模块打交道。

R实例是指rpy2.robjects.r, 它是Python中的嵌入式R进程，把r当作从python走向R的通道来看就可以了。通过R实例，我们可以读取R的内置变量，调用R的函数，甚至直接当做R的解析器来用。

rpy2最近两年的更新好像比较大，如果有些方法用不了，可以参见 https://rpy2.github.io/index_doc.html， 这是rpy2的官方文档，可以在上面查看一些仔细的说明。

首先看一些示例。


```python
from rpy2 import robjects
r=robjects.r

print(r.pi)
print(r['pi'])
```

利用R中的函数

```python
#create a function#
r(
    '''
    f <- function(r){pi*r}
    '''
)
r['f'](3)
```


载入和使用R包，使用rpy2.robjects.packages.importr对象，调用方法是


```python
from rpy2.robjects.packages import importr
stats = importr('stats')
stats.rnorm(10)
```

加载脚本，r.source('script_path')即可将自定义函数加载到全局环境中，再使用r.自定义方法名就可以实现调用。



接下来我们主要关注的是数据类型之间的转换，这个也是最关键的。

数组（包括list）之间的转化


```python
#python的列表 vs R的vector/数组
x=[1,2,3,4]
x=robjects.IntVector(x)
x=['a','b','c']
x=robjects.StrVector(x)

x=r.c(1,2,3,4)
x=list(x3)

#将numpy数组转化为R的数组
import numpy as np
x=np.array([1,2,3,4])
x=robjects.IntVector(x)
#将R的数组转化为numpy数组
x=r.c(1,2,3,4)
print(np.array(x))
```

dataframe之间的转化

```python
##pandas to R
import pandas as pd
x = pd.DataFrame({'x':[1,2,3,4],'y':[2,3,4,5]})
from rpy2.robjects import conversion
from rpy2.robjects import pandas2ri
from rpy2.robjects import default_converter
with conversion.localconverter(default_converter+pandas2ri.converter):
    r_dataframe=conversion.py2rpy(x)
r.print(r_dataframe)

#R to pandas
x=r.c(1,2,3,4)
y=r.c(1,2,3,4)
x=r['data.frame'](x,y)
with conversion.localconverter(default_converter+pandas2ri.converter):
    x=conversion.rpy2py(x)
x.columns=['x','y']
print(x)
```





