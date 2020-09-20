# 其他注意事项

## Python里面的copy

###赋值
在Python里面的赋值语句总是建立一个对象的引用值的，而不是去复制对象的，因此赋值语句是不可能达到copy的效果的. 在下面的代码中，x与y实则指的是同一个对象.
```python
x=[1,2,3,4]
y=x
id(x)==id(y)
```
 因此只有对不可变类型(数字，元组)我们才会用赋值语句去进行copy. 因为其实不可变类型，也就不存在更改的问题。

### 浅拷贝
浅拷贝复制的是第一层对象，因此在没有嵌套类型的复制的时候，浅拷贝可以实现复制的功能。在以下的代码中，我们对alist实现了浅拷贝，当我们对alist的第一层操作时(append)，只有alist改变，而c没有改变。但是当我们改变alist的子对象时，我们发现c对应的子对象相应发生了改变。
```python
import copy
alist=[[1,2],[2,3],4]
c=copy.copy(alist)
alist.append(5)
print(alist)
print(c)
alist[0].append(3)
print(alist)
print(c)
```
因此，在对有嵌套类型的数据类型进行复制的时候，浅拷贝是很容易出现问题的。浅拷贝的方式有很多种，除了借助copy模块之外，很多数据类型都具备copy方法, 如list. 其他如使用列表生成式，for循环之类的拷贝都是浅拷贝.

### 深拷贝
深拷贝才是我们真正意义上的复制，产生一个独立的对象。深拷贝常常要借助于copy模块的deepcopy函数. 如下才算实现了对alist这个列表的真正的复制。
```python
import copy
alist=[[1,2],[2,3],4]
c=copy.deepcopy(alist)
```
值得注意的是, pandas的dataframe具有深拷贝方法`df.copy(deep=True)`, 其deep属性默认就是True,所以不写的话就默认是深拷贝.




