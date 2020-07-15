# Python多进程

#### Python开启进程的方法

```python
import time 
from multiprocessing import Process
def run(name):
    print('Process {} runing '.format(name))
    time.sleep(3)
    print('Process {} running end '.format(name))


if __name__ == '__main__':
    p1=Process(target=run,args=('A',)) #必须加,号
    p2=Process(target=run,args=('B',))
    p3=Process(target=run,args=('C',))
    p4=Process(target=run,args=('D',))

    for p in [p1,p2,p3,p4]:
        p.start()
    print('主线程')
```

大部分的情况下，我们都想让主进程等待子进程结束，这就需要进程的`join`方法，`join`方法等待的是主进程，所以等待的总时间是子进程中耗时最长的那个。将以上代码改成下面这样既可。

```python
for p in [p1,p2,p3,p4]:
	p.start()
for p in [p1,p2,p3,p4]:
	p.join()
print('主线程')
```

值得注意的是，两个`for`循环是不可少的，要等所有的进程`start`了之后才开始`join`，所以不能是 `p.start();p.join()`.



#### 进程池

当我们需要操作的对象不多的时候，还可以用上面的方法来创建进程，但是如果数目太多，用手动的方式去创建进程太过繁琐，因此我们考虑用进程池的方式来创建。其主要语法如下

* `Pool.apply(func,args)`

* `Pool.apply_async(func,args)`

  一个奇怪的点在于 `Pool.apply(func,args)`其实是不能并行计算的，看过一些材料，没看的很明白。推荐使用的是 `Pool.apply_sync(func,args)`.

```python
import time
import numpy as np
from multiprocessing import Pool
def run(name):
    a=np.random.randint(0,10)
    print('Process {} runing, this needs {} seconds '.format(name,a))
    time.sleep(a)
    print('Process {} running end, The return value is {}'.format(name,a))
    return (a)

if __name__ == '__main__':

    p=Pool(4)
    res=[]
    for i in range(8):
        res_temp=p.apply_async(run,args=(i,))
        res.append(res_temp)
    p.close()
    p.join()
    print('主线程')
   	for res_temp in res:
        print(res_temp.get())
```

#### 踩坑

##### 坑一： 关于 `if name=='__main__'` 的应用

在我们目前看到的所有的代码中，我们发现，所有创建子进程的过程都会出现 `if name=='__main__'` 这句。

python中文件的使用有两种方法：

* 作为程序被执行
* 作为模块被其他程序所调用

而 `if name=='__main__'` 的作用就是控制着两种不同的方法执行代码的过程。 在 `if name=='__main__'` 下的代码只有在作为程序被执行的时候才会执行，而被其他程序 import 的时候是不执行的。 

**但是在多进程的时候这个就成了大坑了。**

因为python在创建子进程的时候， 进程会默认导入目前正在运行的文件（也就是将本文件从头到尾开始运行），但是如果我们不用 `if name=='__main__'`的话，子进程会运行到创建子进程这句代码（也是这个文件的一部分），这就陷入了一个无限的循环，而被python所制止，所以一定要加 `if name=='__main__'`. 

但是问题来了，那些成熟的module 如 sklearn, 他们是怎么实现在函数中进行多进程的呢？？？略微查了一下，sklearn 应用的主要是 joblib库，那 joblib库怎么实现的呢？？？暂时我也不知道....巨坑啊.....



## Python 多线程

多线程最简单的方法是直接

```python
from multiprocessing.dummpy import Pool
```

其他用法和多进程一致。 当然多线程还可以用 threading 模块，threading模块的用法和前面的Process比较接近。大多数时候，其实进程池/线程池更加方便， right? 起码我碰到的任务大多数是这样的。

多线程有个不好的地方，在于多线程其实是`并发`而不是`并行`，关于这两个概念的区别可以百度找一下，多线程在处理CPU密集型的任务效果一般般，只有在处理I/O密集型的任务才能真正达到多线程的效果。

但是这个也避免了之前多进程的那个大坑了。



