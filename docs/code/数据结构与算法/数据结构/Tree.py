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


class BinHeap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
    def percUp(self,i):
        while i//2 >0:
            if self.heapList[i]<self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i//2
    def delMin(self):
        ##将最后的叶子节点放到根节点，然后下沉，选择较小的子节点进行下沉
        retval = self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def percDown:
        while (i*2) <= self.currentSize:
            mc =self.minChild(i)
            if self.heapList[i]>=self.heapList[mc]:
                self.heapList[i],self.heapList[mc]=self.heapList[mc],self.heapList[i]
            i = mc
    def minChild(self,i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
