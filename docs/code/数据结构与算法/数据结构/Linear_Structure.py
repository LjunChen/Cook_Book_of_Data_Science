class Stack:
    def __init__(self,a=[]):
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

class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

class List:
    def __init__(self,):
            self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

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

class UnorderedList(Node):
    def __init__(self):
        self.head=None
    def isEmpty(self):
        self.head==None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head =temp
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count =  count +1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head 
        found = False
        while current !=None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current !=None and not found:
            if current.getData() == item:
                    found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


