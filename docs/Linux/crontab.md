### Ubuntu定时任务

Ubuntu的定时任务主要通过crontab命令来管理

其主要用法是:

```
crontab [-u user] {-e|-l|-r}
```

* -u user 指定用户，一般不写
* -e 编辑定时任务
* -l 列出定时任务
* -r 删除定时任务（应该是remove的缩写), 慎用，最好别用，用crontab -e 去修改比较好。



在通过 crontab -e 编辑定时任务时，其主要格式是

```
m h dom mon dow command
```

* m 指定分钟
* h 指定小时
* dom 指定天
* mon 指定月份
* dow 指定周几
* command 指定命令

例如

```
0 1 * * * command
```

表示在每天的 1 :00 执行 command 命令

如果不在root用户下，碰到权限问题，可以考虑用

```
echo 'secret' | sudo command
```

来处理, 这里 secret 是当前用户的 sudo 密码。



