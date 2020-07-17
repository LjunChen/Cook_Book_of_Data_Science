### Ubuntu的terminal的一些用法



#### 文件和文件夹的处理

###### ls的用法

* ls -l  输出详细信息（一般用 ls -lh）
* ls -a 输出全部的文件/文件夹，包括隐藏文件



###### cp的用法

* cp file filecopy 但是这会导致强制覆盖
* cp -i file filecopy 会提示你是否需要overwrite
* cp file folder/ 把文件复制到文件夹
* cp -r folder1/ folder2/ 这里r表示的是recursive
* cp file* folder2/ 将以file开头的文件复制到folder2,当然也可以使用*.py表示以.py结尾的文件



###### mv的用法

* mv file folder/  基础用法



###### mkdir, rmdir, rm 

* mkdir folder 建立一个文件夹
* rmdir folder移除一个文件夹，但是只能移除一个空文件夹
* rm file 直接删除一个文件 也可以加 rm -i 进行interactive
* rm -r foler



###### cat的用法

* cat a.py 在屏幕上显示a.py里面的内容
* cat a.py > b.py 把a.py里面的内容放到b.py里面
* cat a.py b.py > c.py 把a.py, b.py里面的内容都放到c.py
* cat b.py >> a.py 把b.py里面的内容加到a.py后面



#### 自己电脑与服务器的文件互传

```
scp [参数] 原地址 目的地地址
```

如将本地桌上的一个文件传到服务器

```
scp C:/Users/chenl/Desktop/books.pdf sven@120.27.250.172:/home/sven
```

将本地桌上的一个文件传到本地

```
scp sven@120.27.250.172:/home/sven/books.pdf C:/Users/chenl/Desktop
```

如果是传文件夹则是

```
scp -r
```



#### 网络共享

Ubuntu Share文件夹之后需要

sudo smbpasswd -a sven(用户名)

然后会让你创建一个password,共享文献的password

但是这种功能只能在局域网里面实现