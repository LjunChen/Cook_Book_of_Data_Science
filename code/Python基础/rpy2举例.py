#robjetcs
from rpy2 import robjects
r=robjects.r
print(r.pi)

## r packages
from rpy2.robjects.packages import importr
stats=importr('stats')
print(stats.rnorm(10))

r(
    '''
    f<-function(x){pi*x}
    '''
)

print(r['f'](3))
print(r.f(3))##这两种表达都是可以的

##r与python之间的数据类型转换
##数组/list之间的转化
x=[1,2,3,4]
x=robjects.IntVector(x)
r.print(x)
x=['a','b','c']
x=robjects.StrVector(x)
r.print(x)

x=r.c(1,2,3,4)
print(list(x))

import numpy as np
x = np.array([1,2,3,4])
x = robjects.IntVector(x)
r.print(x)

x=r.c(1,2,3,4)
print(np.array(x))


###dataframe 之间的转换

import pandas as pd
x = pd.DataFrame({'x':[1,2,3,4],'y':[2,3,4,5]})
from rpy2.robjects import conversion
from rpy2.robjects import pandas2ri
from rpy2.robjects import default_converter
with conversion.localconverter(default_converter+pandas2ri.converter):
    r_dataframe=conversion.py2rpy(x)
r.print(r_dataframe)

x=r.c(1,2,3,4)
y=r.c(1,2,3,4)
x=r['data.frame'](x,y)
with conversion.localconverter(default_converter+pandas2ri.converter):
    x=conversion.rpy2py(x)
x.columns=['x','y']
print(x)

