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
deb http://mirrors.aliyun.com/CRAN/bin/linux/ubuntu/ focal-cran40/
```

然后

```
apt-get update
```
如果出现未签名错误，The following signatures couldn't be verified because the public key is not acailable:NO_PUBKEY xxxxxxxxxx, 则
```
 sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys  xxxxxxxxxx
```
然后
```
sudo apt-get update
sudo apt-get install r-base-core
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
export PATH="/home/sven/anaconda3/bin:$PATH"
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

* 设置自己的登录密码，复制秘钥，秘钥开头是 sha（好像也未必）

* 修改配置文件

  ```terminal
  vim ~/.jupyter/jupyter_notebook_config.py
  ```

* 然后修改或者直接加入

  ```python
  
  c.NotebookApp.ip='0.0.0.0'              
  c.NotebookApp.password = u'sha:...'      # 刚才复制的那个密文，
  c.NotebookApp.open_browser = False         # 禁止自动打开浏览器
  c.NotebookApp.port =8888       
  c.NotebookApp.all_root=True    ##如果平时是用root用户登录的话可能需要
  c.NotebookApp.notebook_dir=u'/root/' ##平时使用的默认地址
  ```

*  如果是阿里云服务器的话，给阿里云服务器添加安全规则，开放8888端口，其他的服务器可能也需要

* 在terminal输入jupyter notebook即可开始

* 如果是需要后台开启输入 nohup jupyter notebook &

  

  #### pip 换源

  ##### Linux

  * `cd ~`

  * `mkdir ~/.pip`

  * `vim ~/.pip/pip.conf`

  * 输入内容

    ```
    [global]
    timeout = 6000
    
    index-url = https://mirrors.aliyun.com/pypi/simple/
    
    trusted-host = mirrors.aliyun.com
    ```
##### Windows

  * 打开文件资源管理器(文件夹地址栏中)
  
  * 地址栏上面输入 %appdata% (具体是C:\Users\chenl\AppData\Roaming)
  
  * 在这里面新建一个文件夹 pip
  
  * 在pip文件夹里面新建一个文件叫做 pip.ini ,内容写如下和上面一样

  #### Conda换源
  ```
  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls: yes
```

## Ubuntu桌面配置
首先调节显示大小，不然要瞎了。
### 换源
换源是第一步，这个在之前已经有过介绍了，不过在桌面端可以直接使用software manager来换源.

### 安装tweak
```
sudo add-apt-repository universe
sudo apt install gnome-tweak-tool
```
安装tweak.

### 输入法配置
win10还有微软拼音比较好用，而在ubuntu里面只有去装搜狗了. 首先，我们在ubuntu的语言设置里面添加中文.
搜狗输入法是基于fcitx的，因此，我们安装fcitx框架. 
```
sudo apt install fcitx
```
安装好之后，把键盘输入法系统改为fcitx. 然后我们直接去搜狗的官网下载搜狗的安装包，然后直接使用dpkg安装就好了.

### 主题配置
```
sudo apt install gnome-shell-extensions
```
然后需要重启，之后在优化里面找到扩展（不执行上述步骤时扩展里面时空的，shell无法使用扩展），打开User theme. 到此,预备工作完成了.

下面打开[https://www.opendesktop.org/browse/cat/135/order/latest/](https://www.opendesktop.org/browse/cat/135/order/latest/), 选择一款自己喜欢的主题。

[McHigh Sierra](https://www.opendesktop.org/p/1013714/)是一款比较不错的主题.

下载，解压， 然后把目录复制到`/usr/share/themes`.

然后打开优化，我倾向于不改变shell,将应用程序改成`McHigh Sierra`.


### Gnome 扩展设置
直接打开 [https://extensions.gnome.org/](https://extensions.gnome.org/)选择自己想要的扩展.

推荐扩展
* Dash to Dock
* Vitals

### 终端扩展
安装terminator
```
sudo apt install terminator
```
这个需要改一下颜色等配置，太丑了.

### 目录更换
```bash
export LANG=en_US
xdg-user-dirs-gtk-update
```

### 常用软件安装
#### deb 安装
* chrome
* vscode
* 百度网盘
#### gitbook
* nodejs
* npm
* sudo npm install gitbook-cli -g

#### texlive
* 下载最新的texlive的ISO文件
* 安装组件 `sudo apt install perl-tk`
* 加载镜像 `sudo mount -o loop texlive.iso /mnt`
* `cd /mnt`
* `sudo ./install-tl -gui`

安装完成之后，卸载镜像文件
* `cd /`
* `sudo umount /mnt`

然后运行终端看有没有tex命令，如果没有的话,打开`~/.bashrc`加入以下语句
```
export MANPATH=${MANPATH}:/usr/local/texlive/2020/texmf-dist/doc/man
export INFOPATH=${INFOPATH}:/usr/local/texlive/2020/texmf-dist/doc/info
export PATH=${PATH}:/usr/local/texlive/2020/bin/x86_64-linux

```
然后`source ~/.bashrc`






