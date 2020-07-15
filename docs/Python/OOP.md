### Python的类

#### 创建新类

使用 class 语句来创建一个新类，class 之后为类的名称并以冒号结尾, 一般遵循习惯类的名称首字母大写. 以下创建一个简单的类

```python
class Test:
    i=100
    def f(self):
        return ('hello_world')
if __name__ == '__main__':
    a=Test()
    print(a.i) ##访问类的属性
    print(a.f()) ##访问类的方法
```

会输出 100和 'hello world'.  其中 `a=Test()` 这句代码被称为类的实例化。类是一个抽象概念，但是`a`已经是个实例对象了。

##### 类的`_init_()`方法：

这是一个特殊的方法，在类创建的时候会被默认调用，可以用此方法为类传入一些参数

```python
class Test:
    def __init__(self,i):
        self.i=i
    def get_i(self):
        return self.i

if __name__ == '__main__':
    A=Test(10)
    print(A.get_i())
```

我们在创建类的时候，给类传入了一个参数 `i`, 然后我们用类的`get_i`方法返回了类的`i`属性。`get_i`和前面定义的`f` 都是类的方法，类的方法的第一个参数都必须是 `self`，表明是这个类的方法。

##### 类的继承

类是可以继承的，这也是类的一个大的优势，我们可以定义一个基类（父类），然后通过这个基类可以衍生出一些其他的类（子类）。

```python
class People():
    def __init__(self,age,sex):
        self.age=age
        self.sex=sex
    def get_age(self):
        return self.age
class Student(People):
    def __init__(self,age,sex,score):
        People.__init__(self,age,sex) ##这里也可以写sup().__init__(age,sex)
        Student.score=score
if __name__ == '__main__':
    xiaoming=Student(10,'male',100)
    print(xiaoming.get_age())
```

在这个例子中， `Student` 类继承了 `People`类，所以他具有`People`类的属性和方法。如果在父类中的方法不能满足子类的需求的时候，可以在子类中重写。另外，Python支持多继承。

```python
class SonClass(Base1,Base2,Base3):
    pass 	   
```

要注意父类的顺序，如果出现了同名方法，而子类没有重写（子类重写的优先级最高）的话，会按照从左到到右的优先级选择继承哪个父类的方法。

##### 类的私有属性和私有方法

以两个下划线开头，声明该属性或者该方法为类的私有属性或私有方法。类的私有属性或私有方法，只能在类内部被调用，而无法在类的外部被调用。

```python
'''This is a wrong code'''
class Test():
    __name='L'
    def __printhello(self):
        print('hello world')
if __name__ == '__main__':
    A=Test()
    A.__name
    A.__printhello()
```

这句代码会报错。因为 `Test` 这个属性和方法都是私有的，不允许在外部调用的。这么做的目的是为了安全性，防止外界的误操作。另外，关于类的属性（非私有），类的属性是可以被外界修改的，但是我们实际最好还是不要这么做，要对类的属性进行修改，最好是在类中定义一个方法，然后还是操作方法，这种也是为了安全性。

##### 类的 ``__str__``方法

以两个下划线开头，两个下划线结尾的一般都是所有类都有的方法，是Python默认的一些方法。

```python
class Test():
    def __str__(self):
        return 'hello world'

if __name__ == '__main__':
    A=Test()
    print(A)
```

这个方法其实为类定义了`print`这种方法（但是不能用`A.print()`），如果没有这个你选择 `print(A)` 出来的就是这个对象的地址了。所以这个方法其实是很常用的。

我们刚才定义的类的方法实际上应该被称为类的实例方法。因为只能在实例化一个类后，用实例去调用这些方法。

##### 类的静态方法

类的静态方法可以直接使用类名来进行调用，类的静态方法用 `@staticmethod` 装饰，并且不带`self`参数。

#### 类的类方法

 可以被类调用，也可以被实例对象调用, 类方法需要使用关键字`cls`（替代 `self`）,定义时候需要在函数前加`@classmethod`





