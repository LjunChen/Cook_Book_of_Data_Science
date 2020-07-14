# 异常处理

#### Python中的异常

异常是一个事件，当程序运行出现错误的时候，就会发生一个异常。在Python中，异常是一个对象。当Python出现异常的时候，我们需要去捕获这些异常，否则程序就会报错并且终止执行。

常见的异常有：

* IOError 输入/输出异常；基本上是无法打开文件
* ImportError 无法引入模块或包；基本上是路径问题或名称错误
* IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
* KeyError 试图访问字典里不存在的键
* NameError 使用一个还未被赋予对象的变量
* TypeError 传入对象类型与要求的不符合
* ValueError 传入一个调用者不期望的值，即使值的类型是正确的

#### 异常处理



Python中， 捕捉异常一般用 try, except语句。检测 try 语句块中的错误，从而让 except 语句捕获并且处理异常。

try, except 是最简单的结构。还有一些变形。

##### try, except, else 结构

一般来说，程序会尝试执行try 语句里面的内容，如果程序正常执行，会跳过 except语句, 如果还有else语句,则会执行else语句.  如果try语句里面的内容没有正常执行，程序就会去执行 except 语句的内容，并且会跳过 else语句。总结一下就是

* 如果 try 语句顺利执行， 跳过 except, 去执行 else（如果有的话，可以没有else语句）
* 如果 try 语句不能顺利， 会去执行 except, 跳过 else

##### try, except, finally 结构

finally 语句和 else 语句的不同在于

* else 语句仅在程序正常执行（try语句正常执行）的时候才会去执行
* finally语句无论程序是否正常执行都会执行finally语句，在使用这种结构的时候，我们要注意，有时候try语句没有正常执行，会导致一些中间结果的异常，继续执行finally语句可能会继续出现异常（此时的异常没有被捕捉。）

举个简单的例子，我们定义一个函数，将输入的数据转化为整数型,我们可以用try, except 来处理，防止程序报错

```python
def int_convert(x):
	try:
        return int(x)
    except ValueError:
    	print('你的输入无法转化为整数型')
int_convert('abc')
```

程序的结果会打印`你的输入无法转化为整数型`， 而不会直接报错。这里的异常类型是 ValueError. 有时候我们不知道异常的类型， 我们可以直接用 `except Exception`.

> 很多时候，我们想打印出来异常的具体信息，可以考虑用
>
> ```python
> except Exception as e:
> 	print(e)
> ```











 

#### 

