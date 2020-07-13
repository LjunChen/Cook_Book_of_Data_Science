### Python的类



#### 创建新类

使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾, 一般遵循习惯类的名称首字母大写. 以下创建一个简单的类

```python
class Student:   
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
    def get_ID(self):
        return self.ID      
```

