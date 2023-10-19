def registrar_usuarios(self, archivo_empleados, archivo_contraseñas, cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, contraseña, rol="empleado"):

        # Crear un objeto Empleado (o Administrador si es necesario)
        empleado = Empleado(cedula, nombre, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion, rol)

        # Agregar el nuevo empleado al diccionario de empleados
        self.empleados[cedula] = empleado
        # Agregar la contraseña al diccionario de contraseñas
        self.contraseñas[cedula] = contraseña

        # Actualizar el archivo de empleados
        with open(archivo_empleados, "a") as archivo_empleados:
            empleado_info = f"{nombre} {cedula} {fecha_nacimiento} {ciudad_nacimiento} {telefono} {correo} {direccion}"
            archivo_empleados.write("\n")
            archivo_empleados.write(empleado_info)

        # Actualizar el archivo Password.txt (con la contraseña correspondiente)
        with open("Password.txt", "a") as archivo_passwords:
            linea_password = f"{cedula} {contraseña} {rol}"
            archivo_passwords.write("\n")
            archivo_passwords.write(linea_password)

def cambiar_contraseña(self,archivo_contraseñas, cedula, nueva_contraseña):
        if cedula in self.contraseñas:
            print("buscando cedula...")
            # Cambiar la contraseña en el diccionario de contraseñas
            self.contraseñas[cedula] = nueva_contraseña

            with open(archivo_contraseñas, "r") as archivo_passwords:
                lineas = archivo_passwords.readlines()

            with open(archivo_contraseñas, "w") as archivo_passwords:
                for linea in lineas:
                    datos = linea.strip().split(' ')
                    if datos[0] == cedula:
                        linea = f"{cedula} {nueva_contraseña} {datos[2]}\n"
                    archivo_passwords.write(linea)  
                print("contraseña cambiada con exito.")
        else:
            print("Cedula no identificada.")