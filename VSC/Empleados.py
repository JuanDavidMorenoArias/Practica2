#importo mis cosas
from DoubleList import Dlist
from Queue import Queue
from Stack import Stack
from Mensajes import Mensaje


class Empleado():
    def __init__(self, cedula, nombre, fecha_nac, ciudad_nac, telefono, correo, direccion, rol):

        #lo importante
        self.nombre = nombre
        self.cedula = cedula
        #lo que no utilizare
        self.fecha_nac = fecha_nac
        self.ciudad_nac = ciudad_nac
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.rol = rol
        #lo importante
        self.bandeja_entrada = Dlist()
        self.mensajes_leidos = Queue()
        self.borradores = Stack()

    def getName(self):
        return self.nombre
    
    def getId(self):
        return self.cedula
    
    def getEmail(self):
        return self.correo  

    def getRole(self):
        return self.rol

    def encontrar_mensaje_por_numero(self, numero):
        # Método para encontrar un mensaje por número (posición)
        current_message = self.bandeja_entrada.first()
        message_number = 1

        while current_message is not None and message_number < numero:
            current_message = current_message.getNext()
            message_number += 1

        return current_message # encuentra el nodo con el mensaje
    
    def leer_mensaje(self, mensaje):
        # Método para marcar un mensaje como leído
        self.mensajes_leidos.enQueue(mensaje)
        # Elimina el mensaje de la bandeja de entrada
        self.bandeja_entrada.remove(mensaje)  # Debes implementar este método en Listadoble

    def recibir_mensaje(self, mensaje):
        # Método para recibir un mensaje en la bandeja de entrada
        self.bandeja_entrada.addLast(mensaje)

    def revisar_bandeja_entrada(self):
        current_message = self.bandeja_entrada.first()  # Obtén el primer mensaje
        mess_number = 1
        while current_message is not None:
            # Imprime la fecha de recepción, el título y el nombre del remitente
            print(f"Mensaje # {mess_number}")
            print(f"Fecha de recepción: {current_message.getData().getFecha_envio()}")
            print(f"Título: {current_message.getData().getTitulo()}")
            print(f"Remitente: {current_message.getData().getRemitente()}")
            print("---")
            current_message = current_message.getNext()
            mess_number += 1

        # Permite seleccionar un mensaje para leer
        seleccion = input("Elije el número del mensaje que deseas leer (o ingresa 'q' para salir): ")
        if seleccion.lower() == 'q':
            return
        
        # Encuentra el mensaje seleccionado en la lista doble
        selected_message = self.encontrar_mensaje_por_numero(int(seleccion))

        if selected_message is not None:
            # Muestra el contenido del mensaje
            self.leer_mensaje(selected_message.getData())
            print(f"Título: {selected_message.getData().getTitulo()}")
            print(f"Mensaje: {selected_message.getData().getContenido()}")
            print("---")
        else:
            print("Mensaje no encontrado.")

    def guardar_borrador(self,mensaje):
        self.borradores.push(mensaje)

    def redactar_mensaje(self, sistema_mensajeria):
        # Método para redactar un nuevo mensaje
        cedula_destinatario = input("Cédula del destinatario: ")
        titulo = input("Título del mensaje: ")
        mensaje_texto = input("Mensaje: ")

        # Obtener la fecha y hora actual (puedes usar el módulo datetime)

        from datetime import datetime
        fecha_envio = datetime.now()

        nuevo_mensaje = Mensaje(cedula_destinatario, self.cedula, titulo, mensaje_texto, fecha_envio)

        # Buscar al destinatario en el diccionario de empleados del sistema
        destinatario = sistema_mensajeria.obtener_empleado_por_cedula(cedula_destinatario)
        #esto va a ser un objeto de la clase empleado o admin

        if destinatario is not None:
            # Preguntar al usuario qué desea hacer con el mensaje
            opcion = input("¿Qué deseas hacer con el mensaje? (Enviar/Guardar/Descartar): ")

            if opcion.lower() == "enviar":
                # Agregar el mensaje a la bandeja de entrada del destinatario
                destinatario.recibir_mensaje(nuevo_mensaje) #ya cree este metodo para esta clase empleado

            elif opcion.lower() == "guardar":
                # Guardar el mensaje como borrador
                self.guardar_borrador(nuevo_mensaje)

            elif opcion.lower() == "descartar":
                # Descartar el mensaje
                print("Mensaje descartado.")

            else:
                print("Opción no válida. El mensaje se guardará como borrador.")
                self.guardar_borrador(nuevo_mensaje)

        else:
            print("Destinatario no encontrado. El mensaje se guardará como borrador.")
            self.guardar_borrador(nuevo_mensaje)

    def consultar_borrador_actual(self, sistema_mensajeria):

        # Método para ver el último mensaje apilado (borrador actual)
        if not self.borradores.isEmpty():
            mensaje_actual = self.borradores.top() # entrega el objeto
            print("Borrador actual:")
            print(f"Título: {mensaje_actual.getTitulo()}")
            print(f"Mensaje: {mensaje_actual.getContenido()}")

             # Preguntar al empleado qué desea hacer con el borrador
            opcion = input("¿Qué deseas hacer con el borrador? (Enviar/Descartar/Ver Siguiente/Salir): ")
            if opcion.lower() == "enviar":
                destinatario_cedula = mensaje_actual.getDestinatario()
                destinatario = sistema_mensajeria.obtener_empleado_por_cedula(destinatario_cedula)

                if destinatario is not None:

                    destinatario.recibir_mensaje(mensaje_actual)  # Enviar el mensaje al destinatario
                    self.borradores.pop()  # Eliminar el borrador de la pila
                    print("Mensaje enviado.")

                else:

                    print("Destinatario no encontrado. No se pudo enviar el mensaje.")

            elif opcion.lower() == "descartar":
                self.borradores.pop()  # Eliminar el borrador de la pila
                print("Borrador descartado.")


            elif opcion.lower() == "salir":
                return None
            
            else:
                print("Opcion no valida, Saliendo")

        else:
            print("No hay borradores guardados.")

    def revisar_mensajes_leidos(self):
        # Método para revisar los mensajes leídos en orden
        if not self.mensajes_leidos.isEmpty():
            print("Mensajes leídos:")
            while not self.mensajes_leidos.isEmpty():
                mensaje_leido = self.mensajes_leidos.deQueue() # retorna el objeto de la clase mensaje
                print(f"Fecha de recepción: {mensaje_leido.getFecha_envio()}")
                print(f"Título: {mensaje_leido.getTitulo()}")
                print(f"Mensaje: {mensaje_leido.getContenido()}")
        else:
            print("No hay mensajes leídos.")


     
    
    





