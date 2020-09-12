# 数据结构

> Python有个模块叫做Pythonds, 实现了常见的数据结构。

## 线性数据结构

#### 栈
栈(Stack)是一种后进先出（LIFO）的数据结构，
具体代码为
```python
class Stack:
    def __init__(self,a=None):
        self.items=a
    def isEmpty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1] 
    def size(self):
        return len(self.items)
```
#### 队列
队列(Queue)刚好是和栈是相反的,是一种先进先出(FIFO)的数据结构，队列的一个最简单的例子就是排队（可以就这么来理解队列). 我们还是用列表来实现队列
```python
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
```
在这种实现中，入队的复杂度是`O(1)`,而出队的复杂度是`O(n)`.当然，我们可以采用另一种实现来使得入队的复杂度是`O(n)`而出队的复杂度是`O(1)`. 这和栈的实现是不一样的, 在之前的栈的实现中，入栈和出栈的复杂度都是`O(1)`, 这主要是由于Python的list的操作的复杂度来决定的.

#### 双端队列
双端队列有两端，数据项可以从首位两端入队，也可以从首位两端出队.
对双端队列，我们需要定义以下操作:
* `addFront(item)` 将`item`加入队首
* `addRear(item)` 将 `item`加入队尾
* `removeFront()` 从队首移除数据项
* `removeRear()` 从队尾移除数据项
双端队列的实现代码就不在这里赘述了.

### 链表
链表是一种线性数据结构,其中的每个元素实际上是一个单独的对象，而所有对象都通过每个元素中的引用字段链接在一起。
我们首先定义`Node`数据结构
```python
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,newnext):
        self.next=newnext
```
接下来,我们定义无序列表, 重点是添加一个`add`方法,最方便的就是在头部添加，这个Python的List刚好是不一样的.
```python
class UnorderedList(Node):
    def __init__(self):
        self.head=None
    def isEmpty(self):
        self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head =temp
```
当然，我们还需要定义`size,search,remove`等方法. 这是个单项链表，当然我们也可以定义双向链表(有next和previos).

    
#### 散列表

基本概念
* 我们想构造一个数据结构，使得查找算法的复杂度降到 `O(1)`， 这种概念称为"散列"(Hashing)
* 散列表（又称哈希表）是一种数据集，其中数据项的存储方式尤其有利于快速的查找定位。
* 散列表中的每一个存储位置，称为槽（slot），可以用来保存数据项，每个槽有唯一的名称。
* 实现从数据项到存储槽名称的转换的，称为散列函数。

#### 散列冲突

* 两个数据根据散列函数映射到了同一个槽，就会造成冲突，不会造成冲突的叫做完美散列函数，对于一个给定的数据集，我们总是能够设计出一个完美散列函数，但是数据集经常变动，很难有一个系统的方法来设计对应的完美散列函数。

* 近似完美散列函数：`MD5`和`SHA`. `MD5`将任何长度的数据变换为固定长为128位。`SHA-0/SHA-1`输出的散列值160位。

* 散列冲突可以考虑用数据链（每个槽容纳一个集合）或者开放定值法（比如存放到后面最接近的空槽）。 

## 非线性数据结构

#### 树
树是由结点或顶点和边组成的(可能是非线性的)且不存在着任何环的一种数据结构。
树的实现
```python
class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left 
            self.left = t
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRoot(self,value):
        self.value = value
    def getRoot(self):
        return self.value
```

树的遍历:
* 前序遍历
* 中序遍历
* 后序遍历

```python
def preorder(tree):
    if tree:
        print(tree.getRoot())
        preorder(tree.getLeft())
        preorder(tree.getRight())

def postorder(tree):
    if tree !=None:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.getRoot())
def inorder(tree):
    if tree !=None:
        postorder(tree.getLeft())
        print(tree.getRoot())
        postorder(tree.getRight())
```