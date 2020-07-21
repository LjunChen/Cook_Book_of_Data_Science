Hypothesis Testing Framework
$$
\begin{array}{|c|c|c|c|}
\hline & \begin{array}{c}
\text { Declared non- } \\
\text { significant }
\end{array} & \begin{array}{c}
\text { Declared } \\
\text { significant }
\end{array} & \text { Total } \\
\hline \begin{array}{c}
\text { True Null } \\
\text { Hypothesis }
\end{array} & \begin{array}{c}
\mathbf{U} \\
\text { Correct }
\end{array} & \begin{array}{c}
\mathbf{V} \\
\text { Type I Error }
\end{array} & m_{0} \\
\hline \begin{array}{c}
\text { Non-true Null } \\
\text { Hypothesis }
\end{array} & \begin{array}{c}
\mathbf{T} \\
\text { Type II Error }
\end{array} & \begin{array}{c}
\mathbf{S} \\
\text { Correct }
\end{array} & m-m_{0} \\
\hline \text { Total } & m-\mathbf{R} & \mathbf{R} & m \\
\hline
\end{array}
$$

FWER(Familywise/Experimental Error Rate):
<br>
-Probability of making at least one Type I error amongest m independent comparsions $Pr(V\ge 1)$.
<br>
Methods of Controlling FWER:
1. Bonferroni Correction (overly conservative)
2. Holm-Bonferroni method
3. Many more examples: Sidak, Scheffe, Dunnet

FWER is designed for a handful of multiple comparisons, but if we find ourseleves with hundreds of hypothesis tests, we need to control False Discovery Rate(FDR)

FDR is defined as the proportion of rejected hypothesis that are erroneous: V/R 

Benjamini-Hochberg Procedure:
<br>
 $Q=V/(V+S)=V/R$
 <br>
 B-H focus on the expectation of $Q$
 
 1. order m unadjusted p-value generated from m hypothesis test
 2. Let k be largest i for which 
 $$p_{(i)} \le \frac{i}{m} q^{*}$$ where $q^*$ can be set by users, 0.05/0.1/0.01.

3. Reject all $H_i$ for $ i \in (1,2,\dots,k)$


```python
import numpy as np
import pandas as pd
```


```python
data_vec=[0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.000]
#define q^*=0.05
q=0.05
m=len(data_vec)
hold_list=[]
for i in range(1,m+1):
    val=i/m*q
    hold_list.append(val)

combo=pd.DataFrame({'i':range(1,m+1),
                   'p_value':data_vec,
                   'adjusted_p':hold_list})
combo['rejected']=np.where(combo['p_value']<combo['adjusted_p'],1,0)

```


```python
combo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>i</th>
      <th>p_value</th>
      <th>adjusted_p</th>
      <th>rejected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.0001</td>
      <td>0.003333</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.0004</td>
      <td>0.006667</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.0019</td>
      <td>0.010000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.0095</td>
      <td>0.013333</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.0201</td>
      <td>0.016667</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0.0278</td>
      <td>0.020000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0.0298</td>
      <td>0.023333</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0.0344</td>
      <td>0.026667</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>0.0459</td>
      <td>0.030000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>0.3240</td>
      <td>0.033333</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>0.4262</td>
      <td>0.036667</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>0.5719</td>
      <td>0.040000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>0.6528</td>
      <td>0.043333</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>0.7590</td>
      <td>0.046667</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>1.0000</td>
      <td>0.050000</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



* BH is better than FWER
* BH depends upon the independence
* selection of q

Benjamini-Krieger-Yekuteli's Adaptive FDR control
* estimate $k$ and then $\hat{m}_0=m-k$
* $q^*$=$q^{'}m/\hat{m}_0$

Other methods: 
* Storey's postive FDR(p-FDR)
* Local FDR
* Exceedance Control

接下来使用python 的statsmodel模块来处理FDR


```python
import numpy as np
import pandas as pd
from statsmodels.stats.multitest import multipletests
multipletests?
```


```python
data_vec=[0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344, 0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.000]
q=0.05
m=len(data_vec)
result=multipletests(data_vec,alpha=0.05,method='fdr_bh')
combo=pd.DataFrame({'i':range(1,m+1),
                   'p_value':data_vec,
                   'adjusted_p':result[1],
                   'rejected':result[0]})
combo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>i</th>
      <th>p_value</th>
      <th>adjusted_p</th>
      <th>rejected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.0001</td>
      <td>0.001500</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.0004</td>
      <td>0.003000</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.0019</td>
      <td>0.009500</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.0095</td>
      <td>0.035625</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.0201</td>
      <td>0.060300</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>0.0278</td>
      <td>0.063857</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>0.0298</td>
      <td>0.063857</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>0.0344</td>
      <td>0.064500</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>0.0459</td>
      <td>0.076500</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>0.3240</td>
      <td>0.486000</td>
      <td>False</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>0.4262</td>
      <td>0.581182</td>
      <td>False</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>0.5719</td>
      <td>0.714875</td>
      <td>False</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>0.6528</td>
      <td>0.753231</td>
      <td>False</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>0.7590</td>
      <td>0.813214</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>1.0000</td>
      <td>1.000000</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>


