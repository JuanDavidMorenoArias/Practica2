class Mensaje():
    def __init__(self, destinatario, remitente, titulo, contenido, fecha_envio):
        self.destinatario = destinatario
        self.remitente = remitente
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_envio = fecha_envio

    def getRemitente(self):
        return self.remitente
    def getDestinatario(self):
        return self.destinatario
    def getTitulo(self):
        return self.titulo
    def getContenido(self):
        return self.contenido
    def getFecha_envio(self):
        return self.fecha_envio
    
    def setRemitente(self,nuevoRemi):
        self.remitente = nuevoRemi
    def setDestinatario(self,nuevoDesti):
        self.destinatario = nuevoDesti
    def setTitulo(self,nuevoTitulo):
        self.titulo = nuevoTitulo
    def setContenido(self, nuevoContenido):
        self.contenido = nuevoContenido
    def setFecha_envio(self, nuevaFecha):
        self.fecha_envio = nuevaFecha


