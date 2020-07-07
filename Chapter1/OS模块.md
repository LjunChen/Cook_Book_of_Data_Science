### OS模块



#### 目录操作-增删改查

* os.listdir() 列出指定目录下所有的
* os.mkdirs() 创建一个文件夹
* os.rmdir() 删除一个文件夹，但是必须是空文件夹

#### 路径信息

* os.path.abspath(path) 显示当前绝对路径

* os.path.dirname(path) 返回该路径的父目录

  ```python
  os.path.dirname(os.path.abspath('hello.py'))
  ```

* os.path.isfile(path) 是文件则返回True,和os.path.isdir(path)相对应

*  os.path.join(path,name)  #连接目录与文件名或目录 结果为path/name 

* os.getcwd() 显示当前python的工作目录

#### 重命名

```python
os.rename(old_name, new_name)
```





