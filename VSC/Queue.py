from SimpleList import SList
from SimpleNode import SNodo

class Queue():

    def __init__(self):
        self.data = SList()

    def size(self):
        return self.data.size()
    
    def isEmpty(self):
        return self.data.isEmpty() 
    
    def enQueue(self, agregate):
        self.data.addLast(agregate)

    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            return self.data.removeFirst()
    
    def first(self):
        if self.isEmpty():
            return None
        else: 
            return self.data.first().getData()

    