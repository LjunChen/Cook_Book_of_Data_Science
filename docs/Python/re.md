# 正则表达式

参考北京理工大学嵩天老师的《Python网络爬虫与信息提取》课程。

#### 常用函数

1. `re.search(pattern,string,flags=0)`

    在一个字符串搜索匹配正则表达式的第一个位置，返回`match`对象

   `flags` 为正则表达式使用时的的控制标记

   * `re.I` 忽略大小写
   * `re.M` 比如我们要匹配一篇文章，可以对每行进行匹配
   * `re.S`可以让`.`匹配换行符

   ```python
   import re
   match=re.search(r'[1-9]\d{5}','BIT 100081')
   if match:
       print(match.group(0))
   ```

2.  `re.match(pattern,string,flags=0)`

   从一个字符串的开始位置起匹配正则表达式，返回 `match`对象

   ```python
   import re 
   match=re.match(r'[1-9]\d{5}','BIT 100081')
   match.group(0)
   ```

   这是匹配不到的，会报错，match到的是个空的

   ```python
   import re 
   match=re.match(r'[1-9]\d{5}','100081 BIT')
   match.group(0)
   ```

   这是可以匹配到的

3. `re.findall(pattern,string,flags=0)`

```python
import re
ls=re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
ls
```

会输出`[100081 100084]`

4. `re.split(pattern,string,maxsplit=0,flags=0)`

    `maxsplit`: 最大分割数，剩余部分作为最后一个元素输出

   ```python
   import re
   re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
   ```

5.  `re.finditer(pattern,string,flags=0)`

    返回的是个迭代类型，每次匹配的是个`match`对象

   ```
   import re 
   for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
       if m:
           print(m.group(0))
   ```

6. `re.sub(pattern,repl,string,count=0,flags=0)`

   在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

   ```python
   import re
   re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
   ```

   

#### Match 对象

* `.group(0)`获取匹配后的字符串
* `.start()`匹配字符串在原始字符串的开始位置
* `.end()`匹配字符串在原始字符串的结束位置
* `.span()` 返回一个元组 `(.start(),.end())`



#### 匹配符

Re 库默认采用贪婪匹配，即输出匹配最长的子串

##### 最小匹配操作符（加 ？号）

* `*?` 前一个字符0次或无限次扩展，最小匹配
* `+?`前一个字符1次或无限次扩展，最小匹配
* `??` 前一个字符0次或1次扩展，最小匹配
* `{m,n}?`扩展前一个字符m次至n次（含n)，最小匹配

##### 常用操作符

* `.` 表示单个任意字符
* `[]`字符集，对单个字符给出取值范围
* `[^]` 非字符集，对单个字符给出排除范围
* `*` 前一个字符0次或无限次扩展
* `+` 前一个字符1次或无限次扩展
* `?`前一个字符0次或1次扩展
* `|`左右表达式任意一个
* `{m,n}`扩展一个字符m至n次
* `{m}`扩展一个字符m次
* `^`匹配字符串开头
* `$`匹配字符串结尾
* `\d`数字，等价于`[0-9]`
* `()`分组标记，内部职能使用`|`操作符
* `\w` 单词字符，等价于`[A-Za-z0-9_]`



