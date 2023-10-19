class ArrayQueue():

    def __init__(self, capacity):
        self.data = [0]*capacity
        self.first = -1
        self.rear = -1

    # el numero de datos en la cola se calcula aprtir de la ecuacion [(capacity - first + rear)mod capacity] + 1

    def size(self):
        tamaño = len(self.data) - self.first + self.rear
        tamaño = (tamaño % len(self.data)) + 1
        return tamaño
        
    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self, agregate):
        if self.size() < len(self.data):
            self.rear = (self.rear + 1) % len(self.data)
            self.data[self.rear] = agregate
    
    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            eliminado = self.data[self.first]
            self.data[self.first] = None
            self.first = (self.first + 1) % len(self.data)
            return eliminado
        
    def first(self):
        if not self.isEmpty():
            return self.data[self.first]
        else:
            return None



