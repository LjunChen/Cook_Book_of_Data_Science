# git的使用



## git的用户配置

这是为了在每次对版本更改的时候，可以明确身份

* git config --global user.name 'sven'
* git config --global user.email 'chenliujun0556@163.com'



## 建立本地的仓库

* 在git bash中cd 到需要同步的文件夹
* git init 初始化
* touch a.py 一个示例，可以直接创建，或者修改文件也以
* git add a.py 将a.py加入git的管理 
* git commit  -m 'message' 提交修改 
* git log 查看全部的修改记录
* 在 修改之后，git add 之前可以用git diff显示和之前已经commit的对比



## 返回之前的版本

* git commit --amend --no-edit 有时候需要提交的内容和上次的合并（那种忘了，突然加上的小修改）

* git reset a.py 返回到 unstaged 的状态，就是返回add之前
* git reset --hard HEAD~1 回到上次的 ~2回到上两次的

* git log --oneline 显示每次修改的ID
* git reset --head ID 直接回到那一次修改的结果
* git reflog 显示所有的修改记录（包括返回到过去的）
* git checkout ID -- a.py 只针对单个文件返回之前的状态，操作相当于对a.py再做了一次修改



## 分支

* git branch dev 新建一个叫dev的分支
* git branch查看目前所有的分支，*的表示当前所在的分支
* git checkout dev 切换到dev
* git branch -d dev 删除dev分支
* 分支之间是平行的
* git merge --no-ff -m 'message' dev 可以进行分支合并（先切换到主分支)                                     



## 和Github之间的交互

* git remote add origin git@github.com:Sven1996/sven_asus.git(Github中你的仓库的地址) 建立连接
* git push -u origin master 上传文件到Github -u选项第一次加以后可以不加
* 如果push不成功的话加入 git pull --rebase origin master 再进行push
* git remote rm origin 删除origin
* ssh-keygen -t rsa -C "youremail@example.com" 产生本地的公钥
* 中间要求输入密码，可以不输入
* /c/Users/Sven/下有.ssh目录
* 在github的setting的ssh key中加入id_rsa.pub的内容