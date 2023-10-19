from Empleados import Empleado

class SistemaMensajeria:
    def __init__(self):
        self.empleados = {}  # Diccionario para almacenar empleados por cedula
        self.contraseñas = {}  # Diccionario para las claves

    # cargar_empleados leera los archivos para cargar tanto empleados como sus contraseñas

    def cargar_empleados(self, archivo_empleados,archivo_passwords):
        # Leer el archivo Password.txt y crear un diccionario de usuarios y roles
        usuarios_roles = {}
        with open(archivo_passwords, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(' ')
                cedula, contraseña, rol = datos
                usuarios_roles[cedula] = rol
                self.contraseñas[cedula] = contraseña

        # Leer el archivo Empleados.txt y crear objetos Empleado
        with open(archivo_empleados, 'r') as archivo:
            for linea in archivo:
                datos = linea.strip().split(' ')
                cedula = datos[1]
                nombre = datos[0]
                fecha_nacimiento = datos[2:5]
                ciudad_nacimiento = datos[5]
                telefono = datos[6]
                correo = datos[7]
                direccion = datos[8:]

                # Determinar el rol (empleado o administrador) del usuario
                if cedula in usuarios_roles:
                    rol = usuarios_roles[cedula]
                else:
                    rol = "empleado"  # Si no se encuentra en Password.txt, asumimos que es empleado

                if rol == "empleado":
                    empleado = Empleado(cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, "empleado")
                    self.empleados[cedula] = empleado
                elif rol == "administrador":
                    admin = Empleado(cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, "administrador")
                    self.empleados[cedula] = admin

    def verificar_contraseña(self, cedula, contraseña):
        if cedula in self.contraseñas: # busco si la cedula o usuario esta en el diccionario con su respect. clave
            return self.contraseñas[cedula] == contraseña # devyuelve True si la contraseña ingresada concuerda con la del diccionario
        else:
            return False # retorna falso tanto si la contraseña no concuerda como si la cedula no se ha encontrado
  
    def obtener_empleado_por_cedula(self, cedula):
        # Método para obtener un empleado por su cédula
        if cedula in self.empleados:
            return self.empleados[cedula] #entrega objeto de la clase empleado
        else:
            print("Empleado no encontrado.")
            return None

    # Cosas que solo pueden hacer los Admins

    def registrar_usuario(self, cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, contraseña, rol="empleado"):

        # Pregunto si ya esta, porque ¿para que agrego alguien cuya cedula ya esta?
        if cedula in self.empleados and cedula in self.contraseñas:
            print(f"El Usuario con la cedula incertada: {cedula} ya se encuentra en nuestra base de datos")

        else:
            # Crear un objeto Empleado (o Administrador si es necesario)
            empleado = Empleado(cedula, nombre, fecha_nacimiento.split(' '), ciudad_nacimiento, telefono, correo, direccion.split(' '), rol)

            # Agregar el nuevo empleado al diccionario de empleados
            self.empleados[cedula] = empleado
            # Agregar la contraseña al diccionario de contraseñas
            self.contraseñas[cedula] = contraseña
            print(f"El usuario con nombre: {nombre} y cedula: {cedula} ha sido añadido a nuestra base de datos")

    def cambiar_contraseña(self, cedula, nueva_contraseña):
        if cedula in self.contraseñas:
            print("buscando cedula...")
            # Cambiar la contraseña en el diccionario de contraseñas
            self.contraseñas[cedula] = nueva_contraseña
            print("contraseña cambiada con exito.")
        else:
            print("Cedula no identificada.")

    def eliminar_usuario(self, cedula):
        
        # primero me aseguro que la cedula del empleado que voy a eliminar este en ambos diccionarios.
        if cedula not in self.empleados or cedula not in self.contraseñas:
            print("El empleado no se encuentra registrado en el sistema")
        else:
        # Si el usuario se encuentra en mis 2 estructuras de datos, procedo a eliminarlo
            nombre_usuario_eliminado = self.empleados[cedula].getName()
            del self.empleados[cedula]
            del self.contraseñas[cedula]
            print(f"El usuario con nombre: {nombre_usuario_eliminado} y cedula: {cedula} fue eliminado exitosamente")
            
    # Guardar empleados sobreescribira los archivos de texto segun los cambios que se hayan hecho en los diccionarios

    def guardar_empleados(self, archivo_empleados, archivo_passwords):
        # Guardar empleados en Empleados.txt
        with open(archivo_empleados, "w") as archivo_empleados:
            for cedula, empleado in self.empleados.items():
                empleado_info = f"{empleado.nombre} {cedula} {' '.join(empleado.fecha_nac)} {empleado.ciudad_nac} {empleado.telefono} {empleado.correo} {' '.join(empleado.direccion)}"
                print(empleado_info)
                archivo_empleados.write(empleado_info + "\n")
                

        # Guardar contraseñas en Password.txt
        with open(archivo_passwords, "w") as archivo_passwords:
            for cedula, contraseña in self.contraseñas.items():
                rol = self.empleados[cedula].getRole()  
                linea_password = f"{cedula} {contraseña} {rol}"
                print(linea_password)
                archivo_passwords.write(linea_password + "\n")

        for cedula, empleado in self.empleados.items():

            # Guardar borradores
            
            with open(f"{cedula}B.txt", "w") as archivo_borradores:
                if not empleado.borradores.isEmpty():
                    while not empleado.borradores.isEmpty():
                        mensaje = empleado.borradores.pop()
                        archivo_borradores.write("\n")
                        archivo_borradores.write(f"De parte de: {self.empleados[mensaje.getRemitente()].getName()} | Titulo: {mensaje.getTitulo()} | Mensaje: {mensaje.getContenido()} | Fecha: {mensaje.getFecha_envio()}")
            
            # Guardar bandeja de entrada
             
            with open(f"{cedula}BA.txt", "w") as archivo_bandeja:
                if not empleado.bandeja_entrada.isEmpty():
                    current = empleado.bandeja_entrada.first()
                    while current is not None:
                        mensaje = current.getData()
                        archivo_bandeja.write("\n")
                        archivo_bandeja.write(f"De parte de: {self.empleados[mensaje.getRemitente()].getName()} | Titulo: {mensaje.getTitulo()} | Mensaje: {mensaje.getContenido()} | Fecha: {mensaje.getFecha_envio()}")
                        current = current.getNext()

            # Guardar mensajes leídos
            
            with open(f"{cedula}ML.txt", "w") as archivo_leidos:
                if not empleado.mensajes_leidos.isEmpty():
                    while not empleado.mensajes_leidos.isEmpty():
                        mensaje = empleado.mensajes_leidos.deQueue()
                        if mensaje is not None:
                            archivo_leidos.write("\n")
                            archivo_leidos.write(f"De parte de: {self.empleados[mensaje.getRemitente()].getName()} | Titulo: {mensaje.getTitulo()} | Mensaje: {mensaje.getContenido()} | Fecha: {mensaje.getFecha_envio()}")
                

                











base_de_datos = SistemaMensajeria()
base_de_datos.cargar_empleados("Empleados.txt","Password.txt")
base_de_datos.eliminar_usuario("24567898")
for i in base_de_datos.empleados:
    print(base_de_datos.empleados[i].getName())
print('')

#base_de_datos.cambiar_contraseña("Password.txt",'1075689',"hoooooooo")
#print(base_de_datos.contraseñas)

base_de_datos.registrar_usuario("24567898","Juan-Perez","21 06 2004","Medellon","3015194567","jmor@unalledu.co","cll78 south","13556481j")
base_de_datos.registrar_usuario("24567898","Juan-Perez","21 06 2004","Medellon","3015194567","jmor@unalledu.co","cll78 south","13556481j")
print('')
print('')




base_de_datos.empleados['1075689'].redactar_mensaje(base_de_datos)
base_de_datos.empleados['2345934'].revisar_bandeja_entrada()


base_de_datos.guardar_empleados("Empleados.txt","Password.txt")




    


