class SNodo():
    # consta de un dato y su enlace a otros nodos o al vacio en un caso dado
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node
    # gettings y setting del dato y su enlace respectivamente 
    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getNext(self):
        return self.next
 
    def setNext(self, new_next):
        self.next = new_next
    # un ejemplo de clase


