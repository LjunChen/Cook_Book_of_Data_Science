

## 矩阵求导



##### 向量对标量的求导：

一个向量 $$y=(y_1,y_2,\ldots,y_n)^T$$ 对 标量 $$x$$ 的导数就是 $$y$$ 中的每一个元素对 $$x$$ 求导，即
$$
\frac{\partial \mathbf{y}}{\partial x}=\left[\begin{array}{c}
\frac{\partial y_{1}}{\partial x} \\
\frac{\partial y_{2}}{\partial x} \\
\vdots \\
\frac{\partial y_{n}}{\partial x}
\end{array}\right]
$$


##### 矩阵对标量的求导

类似于向量对标量的求导，也就是矩阵的每个元素对 $$x$$进行求导



##### 标量对向量的导数

标量 $$y$$ 关于向量 $$x=(x_1,x_2,\ldots,x_n)^T$$的导数为
$$
\frac{\partial y}{\partial \mathbf{x}}=\left[\frac{\partial y}{\partial x_{1}} \frac{\partial y}{\partial x_{2}} \cdots \frac{\partial y}{\partial x_{n}}\right]
$$

##### 向量对向量的导数

向量 $$y=(y_1,y_2,\ldots,y_n)^T$$ 关于向量 $$x=(x_1,x_2,\ldots,x_n)^T$$的导数为
$$
\frac{\partial \mathbf{y}}{\partial \mathbf{x}}=\left[\begin{array}{cccc}
\frac{\partial y_{1}}{\partial x_{1}} & \frac{\partial y_{1}}{\partial x_{2}} & \cdots & \frac{\partial y_{1}}{\partial x_{n}} \\
\frac{\partial y_{2}}{\partial x_{1}} & \frac{\partial y_{2}}{\partial x_{2}} & \cdots & \frac{\partial y_{2}}{\partial x_{n}} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial y_{n}}{\partial x_{1}} & \frac{\partial y_{n}}{\partial x_{2}} & \cdots & \frac{\partial y_{n}}{\partial x_{n}}
\end{array}\right]
$$

##### 矩阵对向量的导数

矩阵$$Y$$对关于向量 $$x$$的导数，相当于$$Y$$中的每个元素 $$Y_{i,j}$$对 $$x$$ 求导（结果是一个向量 $$n\times 1$$). 将$$Y$$中的每个元素替换成对应的向量。矩阵对矩阵的导数同理定义。



#### 常用公式

假设 $$\beta, x$$都是向量

* $$ \dfrac{\partial \beta^T x}{\partial x}=\beta$$
* $$ \dfrac{\partial x^T x}{\partial x}=2x$$
* $$ \dfrac{\partial x^T A x}{\partial x}=(A+A^T)x$$
* $$ \dfrac{\partial tr(AB) }{\partial A}=B^T$$



