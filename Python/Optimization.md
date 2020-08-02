# Python优化模块

我们考虑用 scipy.optimize 模块来对一些函数求最小值（最大值问题本质上是和最小值是一样的，很容易转换），对方程求根。



#### Minimize: 

```python
scipy.optimize.minimize(fun,x0,args=(),method,bounds,constraints,tol,options)
```

* `func` 目标函数

* `x_0`: 初始值，如果不止一维的话，传入一个numpy的数组

* `args` 目标函数的一些参数

* `method`: 作优化选择的算法，一般常见的有 `Nelder-Mead`,`Newton-CG`,`L-BFGS-B`,`BFGS`,`CG`.

* `bounds`： 参数的bounds, 有约束的优化问题，但是只在 `L-BFGS-B`上可以使用（还可以在`TNC,SLSQP`使用，但是这两个方法没怎么用过), `bounds` 一般的定义方法是`(min_value,max_value)`,例如

  ```python
  bounds=((0,None),(0,None))
  ```

* `constraints`，仅对`SLSQP`可用， constraints 的定义一般通过字典来定义。例如

  ```python
  cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
          {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
          {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})
  ```

* `tol` 控制收敛的条件. 

* `options`， options的定义是一个字典，`tol`也可以在这里设置.

  ```python
  options={'maxiter': 1e6, 'disp': True})
  ```

  主要就两个参数， `maxiter`控制最大迭代次数，`disp`控制是否要打印收敛信息。



#### Root

```python
scipy.optimize.root(fun,x0,args,method,tol,options)
```

定义和前面基本一致，关于method,一般默认的就okay? 具体的不同的方法参见scipy的官方说明文档

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.root.html#scipy.optimize.root.





