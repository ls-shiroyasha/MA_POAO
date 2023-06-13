#Práctica N°4: POO con Python: Almacén de bebidas

class AlmacenBebidas:#Almacén de Bebidas
    #Constructor
    def __init__(self):
        self.bebidas = []
    
    #Métodos
    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    def eliminar_bebida(self, id_bebida):
        for bebida in self.bebidas:
            if bebida.get_idbebida() == id_bebida:
                self.bebidas.remove(bebida)
                break

    def actualizar_bebida(self, id_bebida, nuevo_idbebida, nuevo_nombre, nueva_clasificacion, nueva_marca, nuevo_precio):
        for bebida in self.bebidas:
            if bebida.get_idbebida() == id_bebida:
                bebida.set_idbebida(nuevo_idbebida)
                bebida.set_nombre(nuevo_nombre)
                bebida.set_clasificacion(nueva_clasificacion)
                bebida.set_marca(nueva_marca)
                bebida.set_precio(nuevo_precio)
                break

    def mostrar_tbebidas(self):#Mostrar el total de bebidas
        for bebida in self.bebidas:
            print(f"\nID: {bebida.get_idbebida()}")
            print(f"Nombre: {bebida.get_nombre()}")
            print(f"Clasificación: {bebida.get_clasificacion()}")
            print(f"Marca: {bebida.get_marca()}")
            print(f"Precio: ${bebida.get_precio()}\n")

    def calcular_ppromedio(self):
        total_precio = 0
        for bebida in self.bebidas:
            total_precio += bebida.get_precio()
        return total_precio / len(self.bebidas)
    
    def cantidad_bmarca(self, marca):
        cantidad = 0
        for bebida in self.bebidas:
            if bebida.get_marca() == marca:
                cantidad += 1
        return cantidad
    
    def cantidad_bclasificacion(self, clasificacion):
        cantidad = 0
        for bebida in self.bebidas:
            if bebida.get_clasificacion() == clasificacion:
                cantidad += 1
        return cantidad
    
class Bebida:
    def __init__(self, id_bebida, nombre, clasificacion, marca, precio):
        self.id_bebida = id_bebida
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

    def get_idbebida(self):
        return self.id_bebida
    
    def get_nombre(self):
        return self.nombre
    
    def get_clasificacion(self):
        return self.clasificacion
    
    def get_marca(self):
        return self.marca
    
    def get_precio(self):
        return self.precio
    
    def set_idbebida(self, id_bebida):
        self.id_bebida = id_bebida
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_clasificacion(self, clasificacion):
        self.clasificacion = clasificacion
    
    def set_marca(self, marca):
        self.marca = marca
    
    def set_precio(self, precio):
        self.precio = precio

almacen = AlmacenBebidas()

salir = False

while salir == False:
    print("Almacén de Bebidas")
    print("Seleccione una opción")
    print("(1) Alta de bebidas")
    print("(2) Baja de bebidas")
    print("(3) Actualización de bebidas")
    print("(4) Mostrar todas")
    print("(5) Calcular precio promedio de bebidas")
    print("(6) Cantidad de bebidas por marca")
    print("(7) Cantidad de bebidas por clasificacion")
    print("(s) para salir")

    opcion = input("Seleccione la opción: ")

    if opcion == 's':
        salir = True

    if opcion == '1':#Alta de bebidas
        id = input("ID: ")
        nombre = input("Nombre: ")
        clasificacion = input("Clasificación: ")
        marca = input("Marca: ")
        precio = input("Precio: ")

        bebida = Bebida(id, nombre, clasificacion, marca, precio)
        almacen.agregar_bebida(bebida)
        print("Bebida agregada")
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '2':#Baja de bebidas
        id = input("ID: ")
        almacen.eliminar_bebida(id)
        print("Bebida eliminada")
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '3':#Actualización de bebidas
        id = input("ID: ")
        nuevo_id = input("Nuevo ID: ")
        nuevo_nombre = input("Nuevo Nombre: ")
        nueva_clasificacion = input("Nueva Clasificación: ")
        nueva_marca = input("Nueva Marca: ")
        nuevo_precio = input("Nuevo Precio: ")

        almacen.actualizar_bebida(id, nuevo_id, nuevo_nombre, nueva_clasificacion, nueva_marca, nuevo_precio)
        print("Actualización realizada")
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '4':#Mostrar todas
        almacen.mostrar_tbebidas()
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '5':#Calcular el precio promedio de las bebidas
        print(almacen.calcular_ppromedio())
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '6':#Cantidad de bebidas por marca
        print(almacen.cantidad_bmarca())
        input("Presione cualquier tecla para volver al menu ")

    if opcion == '7':#Cantidad de bebidas por clasificación
        clasificacion = input("Clasificación: ")
        print(almacen.cantidad_bclasificacion(clasificacion))
        input("Presione cualquier tecla para volver al menu ")