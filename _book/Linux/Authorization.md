#### Linux权限

#### 文件权限

用ls -lh可以看到一个文件的权限

e.g. drwxr-xr-x

* 第一位代表 type: d表示文件夹, -表示文件
* 2-4位代表的user的权限，5-7位代表的是group的权限，8-10位代表的是others的权限
* r: read, w:write, x:excute
* 修改文件的权限 
  * chmod u+r t1.py (chmod 是change mod的缩写, u代表user, r是read,全部命令就是赋予user对t1.py的read权限， 这里+可以换成-,表示删除对应的权限)
  * u代表user, g代表group, o代表others, a代表所有, 也可以使用ug表示(user+group)



