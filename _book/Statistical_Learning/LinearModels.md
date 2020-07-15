### Linear Models for Regression

线性模型的优势：

* 简单易解释
* 在小样本, 低 signal-to noise，以及稀疏数据的时候，表现很可能比非线性的模型好
* 线性模型很容易扩展到基函数方法（样条函数）



####  Ridge Regression

岭回归的损失函数如下：
$$
\hat{\beta}^{ridge}=\arg\min_{\beta} \{\sum_{i=1}^N(y_i-\beta_0-\sum_{j=1}^px_{ij}\beta_j)^2+\lambda\sum_{j=1}^p\beta_j^2\}
$$
或者写成矩阵形式：
$$
RSS(\lambda)=(y-X\beta)^T(y-X\beta)+\lambda\beta^T\beta
$$




* 在做岭回归之前，要对输入进行标准化（事实上，对于线性模型都需要做标准化）

* 岭回归有显示解
  $$
  \hat{\beta}^{ridge}=(X^TX+\lambda I)^{-1}X^Ty
  $$
  