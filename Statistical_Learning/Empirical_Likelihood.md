### 经验似然方法

#### 简介

经验似然方法是Owen(1980)提出的一种非参数统计推断方法,不需要假定数据来自一个具体的分布族.

经验似然的主要作用是用来寻找有效的估计，并且构造待估参数（如均值）的置信区间。当然也可以用来做假设检验,这本身就是置信区间的对偶问题.参数模型假定正确的时候，非参数方法达不到参数方法的有效性，但是事实上很多时候，参数模型的假定都是不正确的.
我们经常假定数据是正态的,这种假定在很多时候是合理的，但是也有很多状况下，数据不是正态的，这种时候我们再进行正态性的假定，肯定就是不对的. 因此，现在很多时候大家都倾向于用一些非参数的方法，比如Bootstrap,Jackknife等方法.

相比于Bootstrap来说，由于经验似然方法是用似然函数(likelihood function)，因此当有一些限制的时候，
经验似然方法只需变成有约束的优化问题就可以了，处理起来相对来说很简单.而且,经验似然方法可以用
Bartlett修正来提高推断的精确性.通过Bartlett修正,很多时候可以将置信区间的覆盖错误率降低到
$$O(1/n)$$,达到和参数方法下 MLE 的精度.

#### 随机变量的经验似然

对于一个随机变量 $$X\in \mathbb{R}$$,其累积分布函数(CDF) 是 $$F(x)=Pr(X\le x),-\infty<x<\infty$$. 我们用$$F(x-)$$ 表示 $$Pr(X<x)$$，那么$$Pr(X=x)=F(x)-F(x-)$$. 

$$X_1,\dots,X_n$$ 的经验累积分布函数定义为
$$
F_n(x)=\frac{1}{n} \sum_{i=1}^n 1_{X_i\le x}
$$
假设 $$X_1,\dots,X_n \in \mathbb{R}$$ 独立同分布，其分布函数为 $$F_0$$, CDF的非参数似然定义为 
$$
L(F)=\prod_{i=1}^n(F(X_i)-F(X_i-)).
$$
非参数似然的最大值点就是ECDF, 因此我们可以称ECDF是非参数的极大似然估计.
考虑一个原假设为 $$H_0:T(F_0)=\theta_0$$的经验似然检验,我们定义其 profile的似然比函数为：
$$
\mathcal{R}(\theta)=\sup \{R(F)|T(F)=\theta,F\in \mathcal{F} \}
$$
这里, $$R(F)=\dfrac{L(F)}{L(\hat{F})}$$. 当 $$R(\theta_0)$$小于一个临界值$$<r_0$$的时候，拒绝原假设.这里$$r_0$$的选取可以用经验似然定理.经验似然置信区间的形式如下：
$$
\{ \theta|R(\theta)\ge r_0\}.
$$
均值的profile 经验似然比函数是：
$$
R(\mu)=\max \{\prod_{i=1}^n nw_i|\sum_{i=1}^n w_i X_i=\mu,w_i\ge0,\sum_{i=1}^n w_i=1 \}.
$$
并且其对应的经验似然置信区间是:
$$
\{ \mu|R(\mu)\ge r_0\}=\{ \sum_{i=1}^n w_iX_i|\prod_{i=1}^n nw_i\ge r_0,w_i\ge 0,\sum_{i=1}^n w_i=1\}.
$$
假设 $$X_1,\dots,X_n$$ 是独立同分布的随机变量，其分布函数为 $$F_0$$. 令 $$\mu_0=E(X_i)$$, 并且假设$$0<Var(X_i)<\infty$$. 那么当$$n\to \infty$$时, $$-2\log(R(\mu_0))$$会依分布收敛到一个卡方分布，其自由度为1. 这可以来帮我们选择假设检验问题（和置信区间）中的临界值，当显著性水平为 $$\alpha$$ 时, 如果 $$-2\log R(\mu_0)>\chi^{2,1-alpha}_{(1)}$$，我们就拒绝原假设.

从证明的细节，和一些模拟的结果来看，如果将临界值$$\chi_{(1)}^{2,1-\alpha}$$ 替换为$$F_{1,n-1}^{1-\alpha}$$，效果会更好.有了临界值，我们就可以构造均值的置信区间了,其具体形式如下:
$$
\{ \mu|-2\log R(\mu)\le\chi^{2,1-\alpha}_{(1)} \}=\{\mu| R(\mu) \ge \exp(-\chi_{(1)}^{2,1-\alpha}/2)\}.
$$
在一些比较宽松的矩条件下, 置信区间的覆盖错误率大概以$$O(1/n)$$的速度收敛到0, 这种收敛速度是和参数模型下的极大似然估计是一样的,并且经验似然推断的势和参数模型下的推断差不多，因此经验似然方法能达到很好的精度.
这里 $$R(\mu)$$的计算是一个带约束的优化问题，因此我们考虑用Lagrange乘子法, 简单的计算可以得到
$$
w_i=\dfrac{(X_i-\gamma)^{-1}}{\sum_{j=1}^n (X_j-\gamma)^{-1}},
$$
这里$$\lambda$$ 是下列方程的解
$$
\dfrac{1}{n} \sum_{i=1}^n \dfrac{X_i-\mu}{1+\lambda(X_i-\mu)}=0.
$$


#### 随机向量的经验似然方法

随机向量的经验似然其实就是对随机变量的推广，从一维到多维.首先有一些概念要重新定义一下.假设随机变量
$$X$$的分布函数是 $$F$$, $$F(A)$$ 的意思是 $$Pr(X\in A)$$ 对于$$A\subset \mathbb{R}^d$$. 让 $$\delta_x$$ 表示以概率1，$$X=x$$的一个分布，$$\delta_x(A)=1_{x\in A}$$. $$X_1,\dots,X_n$$的经验累积分布函数为$$F_n=\frac{1}{n} \sum_{i=1}^n \delta_{X_i}.$$ 

假设 $$X_1,\dots,X_n \in \mathbb{R}^d$$独立同分布于共同的分布函数 $$F_0$$, $$F$$的非参数似然是 $$L(F)=\prod_{i=1}^n F(\{ X_i\}).$$ 随机向量的均值的profile经验似然比函数为
$$
R(\mu)=\max \{ \prod_{i=1}^n nw_i |\sum_{i=1}^n w_i X_i=\mu,w_i\ge0,\sum_{i=1}^n w_i=1\}.
$$
构造的置信区间如下
$$
C_{r,n}=\{ \sum_{i=1}^n w_iX_i |\prod _{i=1}^n nw_i \ge r,w_i\ge 0,\sum_{i=1}^n w_i=1\}.
$$

随机变量的 ELT(定理 [\[UniELT\]](#UniELT){reference-type="ref"
reference="UniELT"}) 可以推广到随机向量的情况，

[\[VectorELT\]]{#VectorELT label="VectorELT"} 假设 $$X_1,\dots,X_n$$ 是
$$\mathbb{R}^d$$上的随机向量，其独立同分布于一个共同的分布函数$$F_0$$，其均值是
$$\mu_0$$ ，并且协方差矩阵$$V_0$$有限，秩是 $$q>0$$. 则 $$C_{r,n}$$
是一个凸集并且随着 $$n\to \infty$$， $$-2\log R(\mu_0)$$
收敛到一个自由度是q的卡方分布 $$\chi^2_{(q)}$$.

(A Sketch):

1.  首先证明 $$\mu_0$$ 在 $$X_i$$的凸壳中,

2.  然后说明 Lagrange 乘子的阶是 $$\lambda=O_p(n^{-1/2})$$

3.  说明 $$\lambda=S^{-1}(\bar{X}-\mu_0)+o_p(n^{-1/2})$$，
    $$S$$是样本协方差矩阵

4.  把 $$\lambda$$ 的表达式带入 profile
    经验似然比统计量，然后应用中心极限定理，并且证明其他项的阶更小，是可以忽略的,这样就完成的整个定理的证明.
    具体的证明请参见Owen(1998).

通常情况下,$$V_0$$ 是满秩的 $$q=d$$, 但是如果 $$V_0$$不是满秩的,假设
$$V_0$$的秩是$$q$$的话，我们只需调整卡方分布的自由度就可以了.在实际应用的时候，我们很多时候是不知道$$V_0$$的秩的，这个时候我们一般就用样本协方差矩阵的秩来代替，前提是
$$n \gg d$$. 同样的，和一维的情况（随机变量），定理
[\[VectorELT\]](#VectorELT){reference-type="ref" reference="VectorELT"}
给了我们一种选取临界值$$r$$的方法，在显著性水平为$$\alpha$$的时候，我们选取
$$r=\exp(-\chi_{(q)}^{2,1-\alpha}/2).$$同样，将 $$\chi^2_{(q)}$$ 替换成
$$(n-1)q/(n-q)F_{q,n-q}$$ 效果会更好. As $$n \to \infty$$ 两者其实是等价的.
其实在参数模型里面也是一样，这种 $$F$$修正也是有用的.

####  Fisher, Bartlett, and bootstrap 修正

-   Fisher: 对于正态随机向量 $$X_i$$, 我们知道
    $$n(\bar{X}-\mu_0)^{'} V_0^{-1}(\bar{X}-\mu_0)\sim \chi_{(d)}^2$$.
    但是在 $$V_0$$不知道的情况下,我们一般会选择用 Hotelling's
    $$T^2$$统计量的分布, $$(n-d)T^2/((n-1)d)\sim F_{d,n-d}$$, 这就是
    Fisher修正.

-   Bartlett: Bartlett 修正 是将 $$\chi_{(d)}^{2,1-\alpha}$$ 替换为 :
    $$(1-\frac{a}{n})^{-1} \chi_{(d)}^{2,1-\alpha}, \quad \text{或者} \quad (1+\frac{a}{n})^{-1} \chi_{(d)}^{2,1-\alpha}$$
    这里 $$a$$是一个需要选取的常数. Bartlett
    修正将置信区间的覆盖错误率降低到了 $$O(1/n^2)$$.

-   Bootstrap: 利用 Bootstrap的方法来得到置信域, 当 $$n$$
    比较小的时候，这种方法的效果会比 Bartlett修正好.

#### 均值的光滑函数

假设 $$X_i\in \mathbb{R}^d$$是独立同分布的随机向量，其共同分布为
$$F_0$$，均值为 $$\mu_0$$. 假设 $$h$$ 是一个光滑函数，
$$h:\mathbb{R}^d\to \mathbb{R}^q$$,这里 $$1\le q\le d$$.
我们想要估计的参数是 $$\theta_0=h(\mu_0)$$ ,显然非参数极大似然估计 NPMLE
是 $$\hat{\theta}=h(\bar{X})$$. 其 profile 经验似然比函数是
$$R(\theta)=\max \{ \prod_{i=1}^n nw_i | h(\sum_{i=1}^n w_iX_i)=\theta,w_i\le 0,\sum_{i=1}^n w_i=1 \}.$$

#### 估计方程

我们首先来给出估计方程的定义, 对于一个随机向量 $$X \in \mathbb{R}^d$$,
参数 $$\theta \in \mathbb{R}^p$$,和一个方程
$$m(X,\theta)\in \mathbb{R}^s$$，则 $$E(m(X,\theta))=0,$$
构成了一个估计方程.通常情况下，$$p=s$$, 估计方程只有一个解. 参数的真实值
$$\theta_0$$ 可以通过下面这个方程解出来: $$\label{EstimatingEquation}
\frac{1}{n} \sum_{i=1}^n m(X_i,\hat{\theta})=0$$ 但是有些时候, $$s$$
未必一定等于 $$p$$. When $$s>p$$,方程可能是没有解的.
常用的方法是尽可能找到一个值 $$\hat{\theta}$$去接近
([\[EstimatingEquation\]](#EstimatingEquation){reference-type="ref"
reference="EstimatingEquation"}). 当 $$s<p$$,估计方程
([\[EstimatingEquation\]](#EstimatingEquation){reference-type="ref"
reference="EstimatingEquation"})有 $$s-p$$维的解.

我们定义$$\theta$$的经验似然比函数
$$R(\theta)=\max \{\prod_{i=1}^n nw_i|\sum_{i=1}^n w_im(X_i,\theta)=0,w_i\ge0,\sum_{i=1}^n w_i=1 \}$$
令 $$Y_i=m(X_i,\theta_0)$$,并且
$$Var(Y_i)=Var(m(X_i,\theta_0))$$是有限的并且秩是$$q>0$$, 我们可以从
随机向量的经验似然定理可以直接得到下面的这个定理.

[\[EE ELT\]]{#EE ELT label="EE ELT"} 假设
$$X_i,\dots,X_n\in \mathbb{R}^d$$ 独立同分布于一个共同的分布函数 $$F_0$$.
对于 $$\theta_0 \in \Theta \subseteq \mathbb{R}^p$$, $$X\in \mathbb{R}^d$$ ,
$$m(X,\theta)\in \mathbb{R}^s$$. 令 $$\theta_0 \in \Theta$$ 并且使得
$$Var(m(X_i,\theta_0))$$ 有限,并且秩是 $$q>0$$. 当 $$\theta_0$$ 满足
$$E(m(X,\theta_0))=0$$时,
我们有当$$n \to \infty$$,$$-2\log R(\theta_0)$$依分布收敛到$$\chi^2_{(q)}$$.

定理 [\[EE ELT\]](#EE ELT){reference-type="ref"
reference="EE ELT"}没有任何对$$\theta_0$$的估计$$\hat{\theta}$$的限制，甚至都没有要求$$\theta_0$$存在.因此定理
[\[EE ELT\]](#EE ELT){reference-type="ref" reference="EE ELT"}
可以应用到 $$s=p,s<p,s>p$$的情况.

#### 讨厌参数

当参数集合里面有讨厌参数的时候,我们考虑将我们感兴趣的参数和讨厌参数分开,我们将估计方程写为
$$m(X,\theta,\nu)=0$$, 这里 $$\theta \in \mathbb{R}^p$$ 是我们感兴趣的参数,
$$\nu \in \mathbb{R}^q$$ 是讨厌参数, $$m \in \mathbb{R}^s$$. 参数集合
$$(\theta,\nu)$$ 满足估计方程 $$E(m(X,\theta,\nu))=0$$. 一般来说, $$s=p+q$$.
现在我们定义:
$$R(\theta,\nu)=\max \{ \prod_{i=1}^n nw_i|\sum_{i=1}^n m(X_i,\theta,\nu)=0,w_i\ge0,\sum_{i=1}^n w_i=1  \},$$
以及 $$R(\theta)=\max_{\nu} R(\theta,\nu).$$
我们的方法就是对讨厌参数取使似然函数的最大值,其实也就是把讨厌参数用他们的NPMLE来代替.

#### 分位数

X的$$\alpha$$分位数$$Q^{\alpha}$$的定义是:$$Pr(X\le Q^{\alpha})\ge \alpha$$,并且
$$Pr(X\ge  Q^{\alpha})\le \alpha$$.

这一节,我们不考虑结的情况，并且将分位数的定义简化为
$$E(1_{X\le Q^{\alpha}}-\alpha)=0.$$ 我们定义:$$X_0=-\infty$$
,$$X_{n+1}=\infty$$ 已确保可以包括
$$Q^{\alpha}<X_{(1)}$$和$$Q^{\alpha}\ge X_{(n)}$$的情况.
定义$$Z_i(p,q)=1_{X_i\le q}-p$$， 则分位数经验似然比方程为
$$R(p,q)=\max \{\prod_{i=1}^n nw_i |\sum_{i=0}^{n+1} w_i Z_i(p,q)=0, w_i\ge 0.\sum_{i=0}^{n+1}=1 \}.$$
经过一些简单的计算,我们可以发现:

-   当$$X_{(1)}<q\le X_{(n)}$$, 经验似然比方程为
    $$R(p,q)=(\frac{p}{\hat{p}})^{n\hat{p}}(\frac{1-p}{1-\hat{p}})^{n(1-\hat{p})}.$$
    这里 $$\hat{p}=\hat{p}(q)=\#\{X_i \le q\}/n$$.

-   当 $$q<X_{(1)}$$, 经验似然比方程为 $$R(p,q)=(1-p)^n.$$

-   当 $$q\ge X_{(n)}$$, 经验似然比方程为 $$R(p,q)=p^n.$$

将这三种情况综合起来,就是
$$-\log R(p,q)=n[\hat{p}\log(\hat{p}/p)+(1-\hat{p})\log((1-\hat{p})/(1-p))],$$
这里 $$\hat{p}=\hat{p}(q)=\#\{X_i \le q\}/n$$.

#### 结点和分位数

##### 结点

如果数据有结,假设总共有 $$k$$个不同的取值,记为 $$z_1,\dots,z_k$$, 假设
$$z_j$$出现了　$$n_j$$次, 并且在F下出现的概率是 $$p_j$$.则
$$R(F)=\prod_{j=1}^k (\frac{p_j}{\hat{p}_j})^{n_j}=\prod_{j=1}^k (\frac{np_j}{n_j})^{n_j}.$$
我们可以不考虑结点，并假定每个点在Ｆ下出现的概率分别为 $$w_i$$，只要满足
$$p_j$$是所有的满足　$$X_i=z_j$$的那些$$i$$对应的$$w_i$$相加.而如果不考虑这些约束,$$\prod_{i=1}^n w_i$$的最大值点肯定$$w_i=1/n$$.而考虑这些约束,最大值点肯定是满足　$$w_i=p_{j(i)}/n_{j(i)}=1/n$$,在有没有约束情况下，最大值点都是一样的.
因此实际上,我们可以不考虑这个约束条件.

这也就意味着,结点不会对经验似然方法构造的置信区间产生影响.

##### 结点和分位数

根据我们上一节的讨论，结点在经验似然方法应该不是一个值得关注的问题,因为结点不影响置信区间的构造.　但是我们这一节还是要考虑结点,
原因在于结点会影响我们对分位数的定义.
在3.7那一节,我们假设没有结点,并将分位数的定义简化为$$E(1_{X\le Q^{\alpha}}-\alpha)=0,$$但是实际上我们知道分位数的定义是
$$\label{Quantiledef}
Pr(X\le Q^{\alpha})\ge \alpha,\quad \text{和}\quad Pr(X\ge Q^{\alpha})\ge 1-\alpha.$$
而如果有结点的话，那么这种简化明显是有问题的.一节简单的接近办法就是我们将每个数据随机的加上一个极小的量,
比如我们给每个　$$X_i$$加上一个来源与均匀分布 $$(-A,A)$$的扰动,
这里　$$A$$取非常小的值.这样我们就解决了结点的问题.但即使是没有结点的情况，这种对分位数定义的简化也是有一定偏差的.
一个简单的例子是在t$$n = 2k + 1$$时,样本中位数
$$X_{k+1}$$的经验似然比应该是１,但是$$X_{k+1}$$的经验似然比是
$$(\frac{n}{2k})^k (\frac{n}{2(k+1)})^{k+1} \stackrel{\cdot}{=} 1-\frac{1}{2n}.$$
对于这种中位数估计方程,我们给出一个修正:
$$E(1_{X\le Q^{\alpha}}+\alpha 1_{X=Q^{\alpha}}-\alpha)=0,$$

#### 经验似然的最大似然原理不变性

类似与参数似然中的最大似然原理不变性,经验似然也有类似的性质.

在经验似然中,最大似然原理不变性分为两个方面:

-   参数的变换: if $$\sum_{i=1}^n w_i m(X_i,\theta,\nu)=0$$, then
    $$\sum_{i=1}^n w_i m(X_i,\tau^{-1}(\phi),\nu)=0$$.

-   数据的变换: 假设 $$Y=\tau(X)$$ 是个一一对应的变换. 那么
    $$\sum_{i=1}^n w_im(X_i,\theta)=0$$ 当且仅当
    $$\sum_{i=1}^n w_i m(\tau^{-1}(Y_i),\theta)=0$$.

#### 辅助信息

假设 $$(X,Y)\in \mathbb{R}^2$$,并且我们知道　$$X$$的均值,我们想要构造
$$Y$$的均值的估计和置信区间. 我们定义条件经验似然比函数如下.
首先,我们定义$$R_{X,Y}(\mu_x,\mu_y)$$为
$$\max\{\prod_{i=1}^n nw_i|\sum_{i=1}^nw_iX_i=\mu_x,\sum_{i=1}^nw_iY_i=\mu_y,w_i\ge 0,\sum_{i=1}^n w_i=1   \},$$
并且令
$$R_X(\mu_x)=\max\{\prod_{i=1}^n nw_i|\sum_{i=1}^nw_iX_i=\mu_x,w_i\ge 0,\sum_{i=1}^n w_i=1   \},$$
然后定义
$$R_{Y|X}(\mu_y|\mu_x)=\frac{R_{XY}(\mu_x,\mu_y)}{R_X(\mu_x)}.$$

我们有如下定理:

[\[SideInf\]]{#SideInf label="SideInf"} 假设
$$(X_i,Y_i)\in \mathbb{R}^{p+q}$$是独立同分布的随机向量,其共同分布为$$F_0$$,
均值是 $$(\mu_{x0},\mu_{y0})$$,　方差矩阵满秩，秩为 $$p+q$$. 那么随着
$$n \to \infty$$,
$$-2\log R_{Y|X}(\mu_{y0}|\mu_{x0})$$依分布收敛到$$\chi^2_{(q)}$$ .

定理 [\[SideInf\]](#SideInf){reference-type="ref"
reference="SideInf"}　说明了条件经验似然方程和简单的经验似然方程有相同的渐近分布.
但是,在有辅助信息的情况下,方程是要比没有辅助信息的情况下小的,
因此最后构造的置信域也是要更小一点的.

当估计方程的个数多于未知参数的个数时,　参数推断经常是有问题的.
假设在一个参数模型下, 有　$$p+q$$个估计方程,有　$$q$$个未知参数,
我们可以选择其中的$$q$$个估计方程，忽略其余的$$p$$个.
更加general的来说,　我们可以用这$$p+q$$个估计方程的 $$q$$个线性组合:
$$\label{linCombinEE}
E(m(X,\theta)A(\theta))=0$$ 这里 $$A(\theta)$$ 是
$$(p+q)\times p$$的矩阵，其秩是 $$q$$. 当估计方程$$m$$关于 参数足够光滑的时候,
经验似然方法得到的渐近方差一般来说是要比这种线性组合得到的方差小的,至少是不会比它大的.

假设 $$X_i \in \mathbb{R}^d$$ 是独立同分布的随机向量, 并且假设
$$\theta_0\in \mathbb{R}^p$$ 是被 $$E(m(X,\theta))=0$$　唯一决定的,
这里$$m(X,\theta)\in \mathbb{R}^{p+q}$$, for $$q\ge 0$$. 令
$$\tilde{\theta}=\arg \min_{\theta} R(\theta)$$, 这里
$$R(\theta)=\max \{ \prod_{i=1}^n nw_i |\sum_{i=1}^n w_i m(X_i,\theta)=0,w_i\ge 0,\sum_{i=1}^n w_i=1\}$$
在一些正则条件下, 我们有
$$\lim _{n \to \infty} n Var(\tilde{\theta})=[E(\frac{\partial m}{\partial \theta})^{'}(E(mm^{'}))^{-1}E(\frac{\partial m}{\partial \theta})]^{-1}$$
这个渐近方差是至少不比　([\[linCombinEE\]](#linCombinEE){reference-type="ref"
reference="linCombinEE"})　估计得到的方差大的.并且我们有
$$-2\log(R(\theta_0)/R(\tilde{\theta}))\to \chi^2_{(p)},$$ 以及
$$-2\log R(\tilde{\theta}) \to \chi^2_{(q)}.$$

这个定理的证明在
$$Qin　and Lawless(1994)$$　中有详细的叙述，并且比较复杂，我在这里就不加叙述了.这个定理描述的是独立同分布的状况下，但是其实可以扩展到很多的非独立同分布的状况,这在另一份报告里面有比较详细的描述.

#### 三明治估计量

在估计方程的个数等于参数的个数的时候,即$$r=p$$时,
给定一些比较宽松的正则性条件,$$\sum_{i=1}^n m(X_i,\theta)=0\sum_{i=1}^n m(X_i,\theta)=0$$的解
$$\hat{\theta}$$ 的方差满足
$$n Var(\hat{\theta}) \to I^{-1} C(I^{'})^{-1},$$ 这里 $$\begin{split}
I &=\frac{\partial}{\partial \theta} \int m(X,\theta)d F|_{\theta=\theta_0},\\
C &=\int m(X,\theta_0)m(X,\theta_0)^{'} dF(x).
\end{split}$$
根据以上的公式,我们可以得到$$\hat{\theta}$$的方差的三明治估计
$$\hat{Var}_{Sand}(\hat{\theta})=\dfrac{1}{n} \hat{I}^{-1}\hat{C} \hat{I}^{'-1}.$$

#### 稳健估计

如果数据有异常点的时候, 经验似然构造的置信区间变大.
我们考虑两种方式来达到稳健的效果.第一种是利用一个稳健的估计量,
第二种是对似然函数做一些调增，来达到稳健的效果，这个在下一节会有叙述.这一节我们考虑稳健的估计量.
比如用样本均值来估计总体均值是不稳健的,我们可以考虑用 Huber's-M估计量.
Huber's M估计量是通过求解以下估计方程得到
$$\frac{1}{n} \psi(\frac{X_i-\mu}{\hat{\sigma}})=0$$ 这里 $$\hat{\sigma}$$
是尺度的一个稳健估计, $$\psi(z)=\left \{ \begin{array}{lll}
                -c, && z\le -c \\
                z,&& |z|\le c\\
                c,&& z>c.
\end{array} \right.$$

####  稳健似然

这里，我们考虑第二种达到稳健性的方法:对似然函数做出一定的修正.
考虑数据来源于一个离散分布, $$Pr(X=x;\theta)=f(x,\theta)$$,
并且数据有异常值.也就是说数据$$X_i$$，有 $$1-\epsilon$$ 的概率数据来源于
$$f(x,\theta)$$, 有 where $$\epsilon$$ 的该来了来源于一个未知的分布 $$G_i$$,
这里$$\epsilon>0$$ 是一个很小的数.我们假设观测之间是独立的.那么似然方程为
$$L(\theta,G_1,\dots,G_n)=\prod((1-\epsilon)f(X_i,\theta)+\epsilon G_i(X_i)).$$
取 $$G_i=1$$使似然方程最大化,则,
$$L(\theta,G_1,\dots,G_n)=(1-\epsilon)^n \prod(f(X_i,\theta)+\eta),$$
这里$$\eta=\epsilon/(1-\epsilon)$$.



欧式似然和其他似然
------------------

可以把$$-\sum_{i=1}^n \log(nw_i)$$看成是一种对$$(w_1,\dots,w_n)$$到$$(n^{-1},\dots,n^{-1})$$距离的测度.
那么，一个自然的想法，就是利用其他距离来考虑这个问题，比如欧式距离,KL距离，Hellinger距离,Cressie-Read
power距离. 以欧式距离为例, 欧式对数似然比方程为
$$l_E=-\frac{1}{2} \sum_{i=1}^n (nw_i-1)^2.$$

回归与建模
==========

这一章考虑用经验似然方法来推断广义线性模型.

 随机预测变量
-------------

随机预测和非随机预测变量对应的其实是回归的两种假设. 在非随机预测里面,
我们假设
$$X_i$$是非随机的，更多是我们设计的，所以也被成为设计矩阵,也是之前比较常见的回归模型.
但是现在,
我们很多时候碰到的是观察数据，而不是实验数据，因此认为$$X_i$$也是随机产生的.

假设 $$(X_i,Y_i)$$ 是独立同分布的随机观测. 假设 $$E(X^{'}X)$$ 是满秩的 $$p$$.
$$\beta_{LS}$$的最小二乘估计就是 $$\beta_{LS}=E(X^{'}X)^{-1}E(X^{'}Y)$$
并且对$$\beta_{LS}$$的估计就是(样本代替总体):
$$\hat{\beta}_{LS}=(\frac{1}{n}\sum_{i=1}^n X_i^{'}X_i)^{-1}(\frac{1}{n}\sum_{i=1}^n X_i^{'}Y_i).$$
回归模型可以用估计方程来表示, 根据 $$\beta_{LS}$$的定义, 我们知道
$$E(X(Y-X^{'}\beta_{LS}))=0.$$
定义一个随机变量$$Z_i=Z_i(\beta)=X_i(Y_i-X_i^{'}\beta)$$, $$\beta$$
的经验似然比函数就被定义为
$$R(\beta)=\max \{\prod_{i=1}^n nw_i|\sum_{i=1}^n Z_i(\beta)=0,w_i\ge 0,\sum_{i=1}^n w_i=1 \} .$$

非随机预测变量
--------------

这部分内容,
我们假定$$X_i$$是非随机的.因此我们可以使用给定$$X_1=x_1,\dots,X_n=x_n$$下,
$$Y_1,\dots,Y_n$$的条件似然.
在前一章的时候,我们说明过在给定观测$$\frac{1}{n}\sum_{i=1}^n U_i$$下的条件似然等同于加一个约束条件,$$\sum w_iU_i=E(U)$$.
根据这个思路,我们在计算 $$R(\beta)$$的时候,我们加上这两个约束:
$$\sum_{i=1}^n w_ix_i=\frac{1}{n}\sum_{i=1}^n,$$ 和
$$\sum_{i=1}^n w_ix_ix_i^{'}=\frac{1}{n}\sum_{i=1}^n x_ix_i^{'}.$$

三角阵经验似然定理
------------------

这是一个经验似然应用到独立但是不同分布的例子.

[\[Triangular array ELT\]]{#Triangular array ELT
label="Triangular array ELT"} 假设 $$Z_{in}\in \mathbb{R}^p$$,
$$1\le i\le n$$ ,$$n\ge n_{min}$$ 是一组三角数组排列的随机向量.
假设对于任意的$$n$$, $$Z_{1n},\dots,Z_{nn}$$
都是独立的，并且有共同的均值$$\mu_n$$. 令$$\mathcal{H}_n$$ 表示
$$Z_{1n},\dots,Z_{nn}$$构成的凸壳, 并且令 $$\sigma_{1n}=maxeig(V_n)$$ 以及
$$\sigma_{pn}=mineig(V_n)$$. 假设随着 $$n\to \infty$$,
$$Pr(\mu_n \in \mathcal{H}_n)\to 1$$ 并且
$$\frac{1}{n^2}\sum_{i=1}^n E(||Z_{in}-\mu_n||^4\sigma_{1n}^{-2})\to 0.$$
　　存在 $$c>0$$ 使得对 $$n\ge n_{min}$$,有
$$\frac{\sigma_{pn}}{\sigma_{1n}}\ge c.$$ 则随着$$n \to \infty$$,
$$-2\log R(\mu_n)$$依分布收敛到$$\chi^2_{(p)}$$,这里
$$R(\mu_n)=\max \{ \prod_{i=1}^n nw_i |\sum_{i=1}^n w_i(Z_{in}-\mu_n)=0,w_i\ge 0,\sum_{i=1}^n w_i=1\}.$$

定理
[\[Triangular array ELT\]](#Triangular array ELT){reference-type="ref"
reference="Triangular array ELT"}的证明和独立同分布情况下随机向量的经验似然定理的证明很类似,最大的差别是在中心极限定理的应用上.独立同分布情况下,可以直接用普通的中心极限定理就可以了,但是在这里,我们需要用到
Lyapunov中心极限定理. 定理的条件
$$\frac{1}{n^2}\sum_{i=1}^n E(||Z_{in}-\mu_n||^4\sigma_{1n}^{-2})\to 0$$
是为了满足Lyapunov条件.

ANOVA分析
---------

ANOVA分析主要用来比较不同组之间的均值.
假设我们观测到独立的随机变量$$Y_{ij}\in \mathbb{R}$$,
$$i=1,\dots,k,j=1,\dots,n_i$$. 我们把这些数据重新编码成 N对
$$(I,Y)$$，这里$$I \in \{1,\dots,k\}$$,$$Y\in \mathbb{R}^d$$.这样,观测
$$Y_ij$$可以表示成 $$I=i, Y+Y_{ij}$$. 假设
$$\mu_{i}^0=\int y dF_i^0(y)\in \mathbb{R}^d$$,定义
$$R(\mu_1,\dots,\mu_k)=\max \{ \prod_{i=1}^k \prod_{j=1}^N Nw_{ij}|w_{ij}\ge 0,\sum_{i=1}^k \sum_{j=1}^{n_i}w_{ij}=1,\sum_{j=1}^{n_i} w_{ij}(Y_{ij}-\mu_i)=0,j=1,\dots,k\}.$$

对方差建模
----------

最小二乘估计要求的是$$Y_i$$是一个常数,
如果这个条件不满足了，数据有异方差性，那么用最小二乘来估计，模型就会有偏差.
我们就可以考虑用加权最小二乘估计来提高精确性:

非线性最小二乘
--------------

有些时候,
$$Y$$与$$X$$的关系不是线性的,在不满足线性约束时，我们更加广义的定义最小二乘,通过以下式子来估计
$$\theta$$: $$\arg \min_{\theta} \sum_{i=1}^n (Y_i-f(x_i,\theta))^2,$$
定义 $$g(x_i,\theta)=\frac{\partial}{\partial\theta}f(x_i,\theta)$$,
则估计方程是 $$\sum_{i=1}^n w_i (Y_i-f(x_i,\theta))g(x_i,\theta)=0.$$

广义线性模型
------------

经验似然方法可以应用到广义线性模型上.
广义线性模型一般由残差的分布和连接函数(link function)决定来决定.
这里我们以logistic回归为例，来看这个问题.

假设 $$Y_i \in \{0,1\}$$是独立的, 并且
$$Pr(Y_i=1|X_i=x_i)=\tau(x^{'}\beta)$$,这里 $$\tau(z)=\text{logit} (z)$$,
则估计方程是 $$\sum_{i=1}^n x_i(Y_i-\tau(x_i^{'}\beta))=0.$$
Logistic回归的经验似然推断可以基于以下的经验似然函数
$$R(\beta)=\max \{ \prod_{i=1}^n nw_i |\sum_{i=1}^n Z_i(\beta)=0,w_i\ge 0,\sum_{i=1}^n w_i=1\},$$
这里 $$Z_i(\beta)=x_i(Y_i-\tau(x_i^{'}\beta))$$.

\newpage
\bibliographystyle{plainnat}
