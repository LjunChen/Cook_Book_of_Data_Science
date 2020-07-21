模块rpy2.robjects 是rpy2对R的一个高级封装，使用rpy2的大多数情况，都只需要和这个模块打交道。$\lambda$是一个希腊字母。

R实例是指rpy2.robjects.r, 它是Python中的嵌入式R进程，把r当作从python走向R的通道来看就可以了。通过R实例，我们可以读取R的内置变量，调用R的函数，甚至直接当做R的解析器来用。

首先看一些示例。


```python
from rpy2 import robjects
r=robjects.r

print(r.pi)
print(r['pi'])
```




  


```python
#create a function#
r(
    '''
    f <- function(r){pi*r}
    '''
)
r['f'](3)
```




如何载入和使用R包，使用rpy2.robjects.packages.importr对象，调用方法是


```python
from rpy2.robjects.packages import importr
stats = importr('stats')
stats.rnorm(10)
```










加载脚本，r.source('script_path')即可将自定义函数加载到全局环境中，再使用r.自定义方法名就可以实现调用。

接下来我们主要关注的是数据类型之间的转换，这个也是最关键的。


```python
#python的列表 vs R的vector/数组
x1=[1,2,3,4]
x1=robjects.IntVector(x1)
x2=['a','b','c']
x2=robjects.StrVector(x2)

x3=r.c(1,2,3,4)
x3=list(x3)
```


```python
#将numpy数组转化为R的数组
import numpy as np
x1=np.array([1,2,3,4])
x1=robjects.IntVector(x1)
r.print(x1)
#将R的数组转化为numpy数组
x2=r.c(1,2,3,4)
print(np.array(x2))
```





```python
#将pandas的DataFrame转化为r的data.frame
import pandas as pd 
x=pd.DataFrame({'x':[1,2,3,4],'y':[2,3,4,5]})
from rpy2.robjects import r, pandas2ri 
pandas2ri.activate()
r_dataframe=pandas2ri.py2ri(x)
r.print(x)
#-----------------------------------------
x=r.c(1,2,3,4)
y=r.c(2,3,4,5)
x=r['data.frame'](x,y)
x=pandas2ri.ri2py_dataframe(x)
x.columns=['x','y']
print(x)
```





