这里给出在一个新的Ubuntu服务器上安装我常用的软件及其配置的方法。

## 用户管理

#### 添加用户

```terminal
useradd -s /bin/bash -m -G sudo sven
```

然后使用以下语句设置密码

```
passwd sven
```

#### 删除用户

```
userdel -r sven
```



## 安装R及Rstudio Server

#### 安装R

用 vim 打开/etc/apt/sources.list, 加入

```
deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/
```

然后

```
apt-get update
apt-get install r-base-core
```

#### 安装Rstudio Server

```
sudo apt-get install gdebi-core
wget https://download2.rstudio.org/server/xenial/amd64/rstudio-server-1.3.959-amd64.deb
sudo gdebi rstudio-server-1.3.959-amd64.deb
```

#### 去服务器用户组配置规则8787



## 安装配置python环境

#### Anaconda的安装

下载

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-4.0.0-Linux-x86_64.sh
```

找到对应的文件夹

```
bash Anaconda3-4.0.0-Linux-x86_64.sh
```

#### 配置conda虚拟环境

conda 命令可能用不了

```
vim ~/.bashrc
```

在最后加上

```
export PATH="/root/anaconda3/bin:$PATH"
```

然后

```
source ~/.bashrc
```

再用conda 创造虚拟环境，先查看可用版本

```
conda search "^python$"
```

创造虚拟环境

```
conda create --name sven-Linux python=3.6.2
```

####  Pycharm

配置远程连接服务器的虚拟环境，就可以直接远程同步文件夹，运行本地的代码了

#### jupyter notebook

* 生成配置文件 jupyter notebook --generate-config

* 打开python 生成秘钥

  ```python
  from notebook.auth import passwd
  passwd()
  ```

* 设置自己的登录密码，复制秘钥，秘钥开头是 sha

* 修改配置文件

  ```terminal
  vim ~/.jupyter/jupyter_notebook_config.py
  ```

* 然后修改或者直接加入

  ```python
  
  c.NotebookApp.ip='你的IP地址'                       # 就是多个用户使用ip地址访问
  c.NotebookApp.password = u'sha:...'      # 刚才复制的那个密文，
  c.NotebookApp.open_browser = False         # 禁止自动打开浏览器
  c.NotebookApp.port =8888       
  c.NotebookApp.all_root=True    ##如果平时是用root用户登录的话可能需要
  c.NotebookApp.notebook_dir=u'/root/' ##平时使用的默认地址
  ```

*  如果是阿里云服务器的话，给阿里云服务器添加安全规则，开放8888端口，其他的服务器可能也需要

* 在terminal输入jupyter notebook即可开始

* 如果是需要后台开启输入 nohup jupyter notebook &

  

