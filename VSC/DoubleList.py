from DoubleNode import DNodo 
# Traigo la clase nodo para poder utilizar nodos dobles

class Dlist():
    # constructor, inicializa los atributos head, tail en null y size en 0 como si estuviera vacio
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self): # retorna True si la lista esta vacia, de lo contrario, False
        return self.size == 0

    def size(self): # retorna el tamaño de la lista al momento de ser llamado el metodo
        return self.size
    
    def first(self): # retorna la cabeza de la lista al momento de ser llamado el metodo
        return self.head
    
    def last(self): # retorna la cola de la lista al momento de ser llamado el metodo
        return self.tail
    
    def addFirst(self,data): # convierte data en un nodo doble y lo agrega a la lista como nueva cabeza
        newNode = DNodo(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.size += 1

    def addLast(self,data): # convierte data en un nodo doble y lo agrega a la lista como nueva cola
        newNode = DNodo(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setPrev(self.tail)
            self.tail.setNext(newNode)
            self.tail = newNode
        self.size += 1

    def removeFirst(self): # elimina el nodo cabeza de lista desenlazandolo con el segundo
        if not self.isEmpty():
            eliminado = self.head
            self.head = eliminado.getNext()
            eliminado.setNext(None)
            self.head.setPrev(None) 
            self.size -= 1
            return eliminado.getData()
        else:
            return None
        
    def removeLast(self): # La que era O(n) en las Lsimples, ahora sera O(1)
        if not self.isEmpty():
            eliminado = self.tail
            self.tail = eliminado.getPrev()
            self.tail.setNext(None)
            eliminado.setPrev(None)
            self.size -= 1
            return eliminado
        else:
            return None
        
    # a esta clase se agregaran 3 operaciones basicas de la lista doble
    '''
    def remove(self,doubleNode):
        if doubleNode == self.head:
            return self.removeFirst()
        elif doubleNode == self.tail:
            return self.removeLast()
        else:
            eliminado = doubleNode.getData() # aqui tengo una confusionsilla
            eliminado_prev = doubleNode.getPrev()
            eliminado_next = doubleNode.getNext()

            eliminado_prev.setNext(eliminado_next)
            eliminado_next.setPrev(eliminado_prev)

            doubleNode.setNext(None)
            doubleNode.setPrev(None)

            self.size -= 1

            return eliminado
    '''
    def remove(self, mensaje):
        # Buscar el nodo que contiene el mensaje
        nodo_actual = self.head
        while nodo_actual is not None:
            if nodo_actual.getData() == mensaje:
                break
            nodo_actual = nodo_actual.getNext()

        if nodo_actual is not None:
            # Eliminar el nodo de la lista doble
            if nodo_actual.getPrev() is not None:
                nodo_actual.getPrev().setNext(nodo_actual.getNext())
            else:
                self.head = nodo_actual.getNext()

            if nodo_actual.getNext() is not None:
                nodo_actual.getNext().setPrev(nodo_actual.getPrev())
            else:
                self.tail = nodo_actual.getPrev()

        return mensaje

        
    # nuestros argumentos: 
    # lo que hace addB4 es conectar un nodo que contenga el objeto agregate antes del nodo reference
    # addAfter conecta un nodo que contenga el objeto agregate despues del nodo reference

    def addBefore(self, reference, agregate):
        # caso 1: la referencia es la cabecera
        if reference == self.head:
            self.addFirst(agregate)
        # caso 2: la referencia no es la cabecera
        else: 
            # convierto lo que voy a agregar en un objeto de la clase nodo doble
            newNode = DNodo(agregate)
            # creo una variable para el nodo anterior a la referencia
            beforeRef = reference.getPrev()
            # comienzo a conectar: conecto el nodo anterior al que voy a agregar
            beforeRef.setNext(newNode)
            newNode.setPrev(beforeRef)
            # ahora conecto el que voy a agregar delante y a la referencia
            newNode.setNext(reference)
            reference.setPrev(newNode)

        self.size += 1

    def addAfter(self, reference, agregate):
        # caso 1: reference es la cola
        if reference == self.tail:
            self.addLast(agregate)
        # caso 2: reference no es la cola
        else:
             # convierto lo que voy a agregar en un objeto de la clase nodo doble
             newNode = DNodo(agregate)
             # creo una variable para el nodo posterior a la referencia
             afterRef = reference.getNext()
             # comienzo a conectar: conecto el nodo referencia al que voy a conectar
             reference.setNext(newNode)
             newNode.setPrev(reference)
             # ahora conecto el que voy a agregar delante del posterior a la ref
             newNode.setNext(afterRef)
             afterRef.setPrev(newNode)
             
        self.size += 1














        
            



        
    
        


        



    


    


