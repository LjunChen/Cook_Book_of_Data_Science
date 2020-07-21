import numpy as np

b0=0.5
b1=1
b2=2
x1=np.random.uniform(0,1,1000)
x2=np.random.uniform(0,1,1000)
epsilon=np.random.randn(1000)
y=b0+b1*x1+b2*x2+epsilon

eta=1
e_b0=[]
e_b1=[]
e_b2=[]
e_b0_grad=[]
e_b1_grad=[]
e_b2_grad=[]
e_b0.append(np.random.randn(1))
e_b1.append(np.random.randn(1))
e_b2.append(np.random.randn(1))
for i in range(10000):
    e_b0_grad.append(np.sum(2*(y-e_b0[i]-e_b1[i]*x1-e_b2[i]*x2))/(-1000))
    e_b1_grad.append(np.sum(2*(y-e_b0[i]-e_b1[i]*x1-e_b2[i]*x2)*x1)/(-1000))
    e_b2_grad.append(np.sum(2*(y-e_b0[i]-e_b1[i]*x1-e_b2[i]*x2)*x2)/(-1000))
    e_b0.append(e_b0[i]-eta/np.sum(np.power(e_b0_grad,2))*e_b0_grad[i])
    e_b1.append(e_b1[i]-eta/np.sum(np.power(e_b1_grad,2))*e_b1_grad[i])
    e_b2.append(e_b2[i]-eta/np.sum(np.power(e_b2_grad,2))*e_b2_grad[i])
    if np.abs(e_b0[i]-e_b0[i-1])+np.abs(e_b1[i]-e_b1[i-1])+np.abs(e_b2[i]-e_b2[i-1])<10**-4:
        break


import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
loss=np.zeros(len(e_b2))
for i in range(len(e_b2)):
    loss[i]=np.sum((y-e_b0[i].item()-e_b1[i].item()*x1-e_b2[i].item()*x2)**2)/1000
plt.plot(loss)
plt.title('损失函数图')


print(e_b0[-1])
print(e_b1[-1])
print(e_b2[-1])
print(len(e_b0))