from SimpleList import SList
from SimpleNode import SNodo

# la Stack normal osea esta la utilizo cuando necesite memoria dinamica

class Stack():

    def __init__(self):
        self.data = SList()
    
    def size(self):
        return self.data.size()
    
    def isEmpty(self):
        return self.data.isEmpty() 
    
    def push(self, agregate):
        self.data.addFirst(agregate)

    def pop(self):
        return self.data.removeFirst()
    
    def top(self):
        if not self.isEmpty():
            return self.data.first().getData()#emtrega el objeto no el nodo
        else:
            return None
