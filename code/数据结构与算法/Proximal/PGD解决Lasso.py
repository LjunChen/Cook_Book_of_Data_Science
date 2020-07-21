
def F(y,X,beta,C):
    return 1/2*np.power(y-np.dot(X,beta),2).sum()+C*(np.abs(beta).sum())
def f(y,X,beta):
    return 1/2*np.power(y-np.dot(X,beta),2).sum()
def subf(y,X,beta):
    return np.dot(X.T,np.dot(X,beta)-y)
def prox_L1(beta,C):
    return np.sign(beta)*np.maximum(np.abs(beta)-C,0)


import numpy as np
import pandas as pd
n=500
p=200
s=20
beta=np.append(np.random.normal(0,1,s),np.zeros(p-s))
X=np.random.normal(0,1,(n,p))
y=np.dot(X,beta)+0.1*np.random.normal(0,1,n)



def PGD_LASSO(y,X,beta,C=10,l=1,eta=1.2,maxiter=10000,conv=0.0001):
    opt_F=[]
    for i in range(maxiter):
        grad_x=subf(y,X,beta)
        while True:
            z=prox_L1(beta-grad_x/l,C/l)
            if  f(y,X,z)<f(y,X,beta)+np.dot(grad_x,z-beta)+l/2*np.power(z-beta,2).sum():
                break
            l=eta*l
        beta=z
        opt_F.append(F(y,X,beta,C))
        if i>1 and np.abs(opt_F[i]-opt_F[i-1])<conv:
            print('convergence reached after {} iterations'.format(i))
            break
        if i==(maxiter-1):
            print('algorithm fails to converge')
    return beta,opt_F
beta,opt_F=PGD_LASSO(y,X,beta=np.random.normal(0,1,p))