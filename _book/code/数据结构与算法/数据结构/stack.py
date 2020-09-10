class Stack():
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


##栈的应用，十进制转化为二进制,当然很容易扩展到N进制的数

def divideBy2(decNumber):
    remstack=Stack()
    while decNumber>0:
        rem=decNumber % 2
        remstack.push(rem)
        decNumber=decNumber//2

    binString=""
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())

    return binString


if __name__=='__main__':
    print(divideBy2(42))
