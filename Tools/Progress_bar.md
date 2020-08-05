# Python实现进度条



在处理一些很长时间的循环的时候，我们希望加上**进度条**来帮助我们检测代码执行的进度。



#### 1 利用Python 自己实现进度条的效果

```python
import time
for i in range(10):
    time.sleep(0.5)
    print(('*'*i+' '*(10-i)+'第 {}/{} 轮').format(i+1,10),end='\r')
```

这里的本质是在print输出的时候不换行，在原来的位置刷新输出的值，这里主要是用`\r` 实现的，`\r`的作用是将光标移动到当前行的首行且不换行。

搞清楚了这一步，进度条的实现是不难了。按照自己的需求来打印文本，就可以了。



#### 2 利用tqdm库来实现进度条

tqdm 是一个第三方库，他可以帮助我们轻松实现进度条（主要是好看一点，并且使用起来非常简单）.

```python
from tqdm import tqdm
t=[]
for i in tqdm(range(10)):
    time.sleep(0.5)
```

这样简单的一句就实现了很好的进度条效果（不算特别好看的那种，但是基本够用了）。如果我们需要在迭代过程中更新说明文字，可以使用

```python
bar=tqdm(range(10))
for i in bar:
    time.sleep(0.5)
    bar.set_description('第{}轮'.format(i))
```

