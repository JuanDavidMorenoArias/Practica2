class ArrayStack():

    def __init__(self, capacity):
        self.data = [0] * capacity
        self.top = -1

    def size(self):
        return self.top + 1
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self,agregate):
        if self.top < self.data.len() - 1:
            self.top += 1
            self.data[self.top] = agregate
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            eliminado = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return eliminado
        else:
            return None
        
    def top(self):
        if not self.isEmpty():
            return self.data[self.top]
        else:
            return None