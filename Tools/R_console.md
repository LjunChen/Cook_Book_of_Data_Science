## R从控制台读取输入

R可以使用 readlines 从控制台读取输入，这里n=1表示只能输入一行，如果想读取多行，可以使用`n=-1`（默认的就是这个). 在多行读入时，在windows里面可以使用 `Crlt+Z`然后按回车键结束读入。 Linux系统里面好像是 `Crlt+D`.

```R
cat("Enter your name : ")
name <- readLines(file("stdin"),n=1)
cat("Enter your age : ")
age <- readLines(file("stdin"),n=1)
print(paste0('hello, ',name, 'your age is ', age))
```

