### python文件处理



#### open 方法

Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

**注意：**使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

open() 函数常用形式是接收两个参数：file, mode, encoding。

```python
open(file, mode='r',encoding=None)
```

mode 参数常用的有

* r 只读
* a+ 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
* w+ 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。



#### file 对象

* file.close() 关闭文件
* file.seek() `0代表从头开始，1代表当前位置，2代表文件最末尾位置`
* file.readlines()
* file.writelines()



