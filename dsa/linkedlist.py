class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self,data):
        node = Node(data)
        node.ref = self.head
        self.head = node
        
    def printLL(self):
        n=self.head
        while n is not None:
            print(n.data,"--->",end=' ')
            n=n.ref
        
LL1 = LinkedList()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.add_begin(300)
LL1.printLL()
