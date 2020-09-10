from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston=load_boston()
X_train,X_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=0)

###构建管道
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
import numpy as np
pipe=Pipeline([('scaler',StandardScaler()),('svm',SVR())])
pipe.fit(X_train,y_train)
pred = pipe.predict(X_test)
np.mean(np.power(pred-y_test,2))


from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
pipe=make_pipeline(StandardScaler(),PolynomialFeatures(),Ridge())
param_grid={'polynomialfeatures__degree':[1,2,3],'ridge__alpha':[0.001,0.01,1]}
grid = GridSearchCV(pipe,param_grid=param_grid,cv=3,n_jobs=-1)
grid.fit(X_train,y_train)
