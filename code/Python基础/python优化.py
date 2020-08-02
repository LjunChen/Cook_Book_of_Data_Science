from scipy.optimize import minimize
import numpy as np


def rosem(x):
        return sum(100.0*(x[1:]-x[:-1])**2.0+(1-x[:-1])**2.0)


x0=np.array([1.3,0.7,0.8,1.9,1.2])
res=minimize(rosem,x0,method="nelder-mead",options={"tol":1e-8,"disp":True})
print("rose mini:",res)#求函数最小值
print("rose mini:",res.x)
