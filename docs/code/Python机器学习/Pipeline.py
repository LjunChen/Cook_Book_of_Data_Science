from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
boston=load_boston()
X_train,X_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=0)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
pipe=make_pipeline(StandardScaler(),PolynomialFeatures(),Ridge())
param_grid={'polynomialfeatures__degree':[1,2,3],'ridge__alpha':[0.001,0.01,1]}
grid = GridSearchCV(pipe,param_grid=param_grid,cv=3,n_jobs=-1)
grid.fit(X_train,y_train)
plt.matshow(grid.cv_results_['mean_test_score'].reshape(3, -1),
        vmin=0, cmap="viridis")
plt.xlabel("ridge__alpha")
plt.ylabel("polynomialfeatures__degree")
plt.xticks(range(len(param_grid['ridge__alpha'])), param_grid['ridge__alpha'])
plt.yticks(range(len(param_grid['polynomialfeatures__degree'])),
        param_grid['polynomialfeatures__degree'])
plt.colorbar()
plt.show()