### Splines

#### Basics

立方样条(cubic spline)是指有连续的一阶和二阶导数的样条函数。

更一般地，一个M阶样条，是一个由最高为M阶的多项式的基展开的，并有连续的 $M-2$ 阶导数。立方样条的$M=4$.

自然立方样条（nature cubic spline) 加上一个限制，要求超出边界节点部分是线性的。

自然立方样条(K个节点)的基为
$$
N_1(X)=1,N_2(X)=X, N_{k+2}(X)=d_k(X)-d_{K-1}(X),
$$
where
$$
d_{k}(X)=\dfrac{(X-\xi_k)_{+}^3-(X-\xi_K)_{+}^3}{\xi_K-\xi_{k}}.
$$

#### Smoothing Splines 光滑样条



对 $f(x)$的复杂程度做惩罚
$$
RSS(f,\lambda)=\sum_{i=1}^N(y_i-f(x_i))^2+\lambda\int (f^{''}(t))^2dt
$$


