# 算法链和管道

对于一个机器学习问题来说，我们需要对数据进行预处理，然后再进行模型的训练。某些机器学习项目还需要使用多个算法的结合。

使用管道 Pipeline 可以简化这一过程，减少代码的使用量，特别是在与网格搜索的过程结合时，可以起到显著的作用。另外，Pipeline可以很好的帮助我们进行数据预处理。我们知道，当我们拿到一个数据集之后，我们首先要将数据分成训练集和测试集，如果我们要对数据进行缩放，我们只能利用训练集中的数据来训练 StandardScaler(), 而不能以整个数据集来训练。但是如果我们要自己这样写代码就会显得有些臃肿，而用Pipeline可以让你的代码看上去很整洁。

我们接下来用boston的房价数据为例。先导入数据

```
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston=load_boston()
X_train,X_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=0)
```



#### 构建管道

我们首先构建一个数据标准化+SVM的管道来处理boston的房价问题

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np
pipe=Pipeline([('scaler',StandardScaler()),('svm',SVR())])
pipe.fit(X_train,y_train)
pred = pipe.predict(X_test)
np.mean(np.power(pred-y_test,2))
```

结果不怎么好，这也很正常，毕竟我们参数也没调, 但是这里我们使用管道构建了一个机器学习的方法（减少了很多的代码量。）



#### 网格搜索中使用管道

在我看来，这个地方的应用才是管道最大的优势所在，下面我们考虑 缩放特征+计算多项式特征+岭回归来处理刚才的Boston房价问题。我们知道多项式特征变换中，我们要确定选择几阶多项式（degree）,在岭回归中，我们要选择惩罚的系数alpha.

```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
pipe=make_pipeline(StandardScaler(),PolynomialFeatures(),Ridge())
param_grid={'polynomialfeatures__degree':[1,2,3],'ridge__alpha':[0.001,0.01,1]}
grid = GridSearchCV(pipe,param_grid=param_grid,cv=3,n_jobs=-1)
grid.fit(X_train,y_train)

```

用管道写出来的代码真的及其简单。这里我们用到了make_pipeline函数，这和前面的Pipeline实质上是一致的，在Pipeline函数中，我们需要对每一步的处理命名，而在make_pipeline中省略了这一步（自动命名了）.

