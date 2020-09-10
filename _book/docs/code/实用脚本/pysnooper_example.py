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
