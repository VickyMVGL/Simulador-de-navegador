class ArchivoDescargas:
    def __init__(self, nombre, fecha, tamano):
        self.nombre = nombre
        self.fecha = fecha
        self.tamano = tamano
        self.siguiente = None
        
    class ColaArchivos:
        def __init__(self):
            self.cabeza = None
            self.cola = None

        def agregar_archivo(self, nombre, fecha_creacion, fecha_modificacion, tamano,
        contenido):
            nuevo_nodo = ArchivoDescargas(nombre, fecha_creacion, fecha_modificacion, tamano,
            contenido)
            if not self.cabeza:
                self.cabeza = nuevo_nodo
                self.cola = nuevo_nodo
            else:
                self.cola.siguiente = nuevo_nodo
                self.cola = nuevo_nodo


        def mostrar_archivos(self):
            actual = self.cabeza
            while actual:
                print("Nombre:", actual.nombre)
                print("Fecha:", actual.fecha)
                print("Tamaño:", actual.tamano)
                print()
            actual = actual.siguiente


        def buscar_archivo(self, nombre):
            actual = self.cabeza
            while actual:
                if actual.nombre == nombre:
                    return True
                actual = actual.siguiente
            return False
        
        def eliminar_archivo(self):
            if not self.cabeza:
                return None
            eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return eliminado