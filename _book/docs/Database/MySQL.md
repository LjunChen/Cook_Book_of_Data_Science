## 索引

索引可以帮助快速的查找数据，提高查询的效率。

索引建立方法, 如果要建立的索引字段是字符串，最好写上字符串的长度。以下是在test表中对id字段建立索引。

```mysql
create index 索引名称 on 表名(字段名(长度))
```

删除索引

```mysql
drop index 索引名称 on 表名
```

查看索引

```mysql
show index from 表名
```

主键，外键其实都是一种索引

常用的列，并且数据量很大，才会考虑使用索引。索引太多容易影响更新和插入的速度。