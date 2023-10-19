from SimpleNode import SNodo
# Una lista simple: Coleccion de Nodos simples enlazados a travez del atributo Next
# es parecido al arreglo, pero hace mejo uso de memoria al no permitir indexacion de posiciones especificas
class SList():

    # Constructor, inicializa los atributos de una lista como si estuviera vacia

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # retorna True si la lista esta vacia, de lo contrario, False
    def isEmpty(self):
        return self.size == 0
    # getting y setting del atributo Size
    def size(self):
        return self.size   
    def setSize(self,s):
        self.size = s
    # Gettings de la cabeza y la Cola
    def first(self):
        return self.head   
    def last(self):
        return self.tail
    # Settings, pero estos requieren enlazar y mover tanto cabezas como colas 
    def addFirst(self,data):
        newNode = SNodo(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.size += 1

    def addLast(self,data):
        newNode = SNodo(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1
    # Remover o eliminar, eliminar la cola(removeLast) es la unica operacion O(n), todo lo demas es constante
    def removeFirst(self):
        if not self.isEmpty():
            eliminado = self.head
            self.head = eliminado.getNext()
            eliminado.setNext(None)
            self.size -= 1
            return eliminado.getData() #retorna el objeto, no el nodo
        else:
            return None
    def removeLast(self):
        # si la lista solo tiene un elemento, se borra ese con el metodo anterior
        if self.size == 1:
            self.removeFirst()
        # si la lista tiene mas de 1 elemento, se hace asi
        elif not self.isEmpty():
            eliminado = self.tail
            anterior = self.head
            while anterior.getNext() != self.tail:
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.tail = anterior
            self.size -= 1
            return eliminado.getData()
        # si la lista no tenia elementos para eliminar
        else:
            return None







    

