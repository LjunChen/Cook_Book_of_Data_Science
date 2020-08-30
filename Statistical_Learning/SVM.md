## SVM

我们知道一个 n 维空间里面超平面的定义为 $$ \{ x: w^T x+b=0\}$$.
空间中任意一点 x 到超平面的距离为 $$|w^Tx+b|/||w||_2$$.

我们假设有一个超平面可以很好的将样本分割开，则
$$
\left \{ 
\begin{array}{ccc}
w^Tx_i+b \ge c & & y_i=1 \\
w^Tx_i+b \le -c & & y_i=-1
\end{array}
\right.
$$
于是支持向量到超平面的距离之和为 $$2c/||w||_2$$. 这里c是一个常数，因此我们的目标等价
$$
\min 1/2 ||w||_2^2 \quad s.t. y_i(w^Tx_i+b_i)\ge 1, i=1,2,\ldots,n
$$
现在我们将其转化为对偶问题
$$
L(w,b,\lambda)=1/2||w||_2^2+\sum_{i=1}^n \lambda_i(1-y_i(w^Tx_i+b))
$$
对 $$w,b$$求导，并令导数等于0，我们可以得到
$$
w=\sum_{i=1}^n \lambda_iy_ix_i, \sum_{i=1}\lambda_iy_i=0
$$
将其代入 $$L$$ 中，我们可以得到
$$
L=-1/2\sum_{i=1}^n \sum_{j=1}^n \lambda_i\lambda_jy_iy_jx_i^Tx_j+\sum_{i=1}^n \lambda_i
$$
所以原问题的对偶问题是
$$
\max_{\lambda}L, \quad s.t. \lambda_i\ge 0,\sum_{i=1}^n\lambda_iy_i=0
$$

#### Kernel

对于使用kernel的SVM，其原问题是
$$
\min 1/2 ||w||_2^2 \quad s.t. y_i(w^T\phi(x_i)+b_i)\ge 1, i=1,2,\ldots,n
$$
其对偶问题是
$$
\max_{\lambda} -1/2\sum_{i=1}^n \sum_{j=1}^n \lambda_i\lambda_jy_iy_j\phi(x_i)^T\phi(x_j)+\sum_{i=1}^n \lambda_i
$$
我们会假设存在一个核函数使得 $$K(x_i,x_j)=\phi(x_i)^T\phi(x_j)$$.

最常用的核函数是高斯核（也被称为RBF） $$K(x_i,x_j)=\exp(-||x_i-x_j||^2/2\sigma^2)$$.

#### 软间隔的SVM

在前面的讨论中，我们是假设存在了一个超平面，使得样本能够被这个超平面完全分割开。但是在很多时候，这都是没办法办到的。

我们允许SVM在少量样本中出错就可以解决这个问题。引入松弛变量，我们可以将目标函数写为
$$
\min 1/2||w||_2^2+C\sum_{i=1}^n \xi_i \quad s.t. y_i(w^Tx_i+b)\ge 1-\xi_i, \xi_i \ge 0.
$$
