### Proximal Gradient

一般的非线性优化问题主要是通过Gradient Descent方法来解决的。但是这必须要求目标函数是可导的，但是实际上，我们经常会碰到一些目标函数不可导的优化问题（如LASSO,分位数回归等）。Proximal Gradient  (以下简称PG) 算法主要是为了解决一类不可导无约束优化问题（大部分的有约束优化问题也可以通过 Lagriange 方法转化为无约束优化问题。）

我们考虑如下的优化问题：
$$
\min_{x} F(x)=f(x)+g(x)
$$
这里我们要求$$f(x)$$是可导的，凸的，并且是 $$\beta$$-Smooth的，但是对于$$g(x)$$我们只要求 $$g(x)$$是凸的（其实很多的非凸问题也可以用Proximal Gradient Descent 来解决，不过理论证明会相对比较复杂，所以这里我们假设函数都是凸函数）。

这种问题有很多，例如

* 投影问题 ，可以写做
  $$
  \min_{x} f(x)+\delta_{C}(x)
  $$
  其中，如果 $$x\in C,\delta_{C}(x)=0$$，否则 $$\delta_{C}(x)=\infty$$. 这里$$C$$是我们需要投影的空间。

* Lasso 问题
  $$
  \min_{x} \dfrac{1}{2}||y-Ax||^2+\lambda ||x||_1
  $$

####  Proximal Gradient 算法

我们构建 $$F(x)$$的一个upper bound.

我们定义
$$
m(x)=f(x_t)+<\nabla f(x_t),x-x_t>+\frac{\beta}{2} ||x-x_t||^2+g(x).
$$
由于 $$f(x)$$ 是 $$\beta$$ smooth的，所以 $$m(x)\ge f(x)+g(x)$$.

很容易验证（配方），
$$
m(x)=f(x_t)-\dfrac{1}{2\beta}||\nabla f(x_t)||^2+\dfrac{1}{2\beta}||x-(x_t-\dfrac{1}{\beta}\nabla f(x_t))||^2+g(x)
$$
我们定义
$$
x_{t+1}=\arg\min_{x} m(x),
$$
则 $$F(x_{t+1})\le m(x_{t+1})\le m(x_t)=f(x_t)+g(x_t)=F(x_t)$$. 

由于我们是对 $$x$$ 求最小($$m(x)$$的前两项和$$x$$无关)，所以
$$
x_{t+1}=\arg\min_{x} \dfrac{1}{2\beta}||x-(x_t-\dfrac{1}{\beta}\nabla f(x_t))||^2+g(x).
$$
我们定义
$$
Prox_{g}(t)=\arg\min_{x}\{\dfrac{1}{2}||x-t||^2+g(x)\}.
$$
则 
$$
x_{t+1}=Prox_{\frac{1}{\beta}g}(x_t-\dfrac{1}{\beta}\nabla f(x_t)).
$$
这里 $$\dfrac{1}{\beta}$$实际上是迭代过程中的步长, 记为 $$t_k$$.(如果 $$f(x)$$ 是一个$$\beta$$ smooth的函数，则步长就取 $$1/\beta$$. 但是实际上，我们有时候很难求这个 $$\beta$$， 或者 $$f(x)$$也可能不是 $$\beta$$ smooth的，因此我们考虑更一般的步长 $$t_k$$)。

完整的 Proximal Gradient 算法叙述如下.

**Initialization**: 选择 $$x_0$$

**General Step** 对于$$t=0,1,2,\cdots$$, 执行

* 选择步长 $$t_k$$

* $$
  x_{t+1}=Prox_{t_k g}(x_t-t_k\nabla f(x_t)).
  $$




#### Proximal 算子的计算









### ADMM 算法

带约束的优化问题

1)QP问题可以直接用拉格朗日法求解

2）ADMM算法
$$
H_{opt}=\min \{ H(x,z)=h_1(x)+h_2(z): Ax+Bz=c\}
$$


这里我们假设: $$h_1$$和$$h_2$$ are proper closed and convex functions.



> ADMM
>
> Initialization : $$x^0\in R^n, z^0 \in R^p, y^0\in R^m ,\rho>0$$
>
> General Step: for any $k=0,1,...$ excute the following:
>
> (a) $$x^{k+1}\in \arg\min_x \{ h_1(x)+\frac{\rho}{2} ||Ax+Bz^k-c+\frac{1}{\rho}y^k||^2\}$$
>
> (b)$$z^{k+1}\in \arg\min_z \{ h_2(z)+\frac{\rho}{2} ||Ax^{k+1}+Bz-c+\frac{1}{\rho}y^k||^2\}$$
>
> (c) $$y^{k+1}=y^k+\rho(Ax^{k+1}+Bz^{k+1}-c)$$





> AD-LPMM
>
> Initialization: $$x^0\in R^n, z^0 \in R^p, y^0\in R^m ,\rho>0, \alpha \ge \rho \lambda_{max}(A^TA),\beta\ge \rho\lambda_{max}(B^TB)$$
>
> General Step: for any $k=0,1,...$ excute the following:
>
> (a) $$x^{k+1}=prox_{\frac{1}{\alpha}h_1} [x^k-\frac{\rho}{\alpha}A^T(Ax^k+Bz^k-c+\frac{1}{\rho}y^k)]$$
>
> (b) $$z^{k+1}=prox_{\frac{1}{\beta}h_2}[z^k-\frac{\rho}{\alpha}B^T(Ax^{k+1}+Bz^k-c+\frac{1}{\rho}y^k)]$$
>
> (c) $$y^{k+1}=y^k+\rho(Ax^{k+1}+Bz^{k+1}-c)$$



