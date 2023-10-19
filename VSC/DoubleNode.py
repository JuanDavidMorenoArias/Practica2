class DNodo():
    # consta de un dato y su enlace a otros nodos o al vacio en un caso dado, ahora en ambas direcciones
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
        
    # gettings y setting del dato y sus enlaces respectivamente 
    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getPrev(self):
        return self.prev
 
    def setPrev(self, new_prev):
        self.prev = new_prev

    def getNext(self):
        return self.next
 
    def setNext(self, new_next):
        self.next = new_next

    
 

