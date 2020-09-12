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
