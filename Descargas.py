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

    def agregar_descarga(self, nombre, fecha_creacion, tamano):
        nuevo_nodo = ArchivoDescargas(nombre, fecha_creacion, tamano)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo


    def mostrar_descarga(self):
        actual = self.cabeza
        while actual:
            print("Nombre:", actual.nombre)
            print("Fecha:", actual.fecha)
            print("Tamaño:", actual.tamano)
            print()
            actual = actual.siguiente


    def buscar_descarga(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return True
            actual = actual.siguiente
        return False
        
    def eliminar_descarga(self):
        if not self.cabeza:
            return None
        eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminado
        
    def cola_vacia(self):
        return self.cabeza is None

    def guardar_estado_descargas(self, archivo_csv='descargas.csv'):
        with open(archivo_csv, 'w') as file:
            file.write("URL,Fecha,Tamagno\n") 
            actual = self.cabeza
            while actual:
                file.write(f"{actual.nombre},{actual.fecha},{actual.tamano}\n")
                actual = actual.siguiente
        print(f"Estado de descargas guardado en {archivo_csv}.")


"""

cola = ColaArchivos()

# Agregar archivos a la cola de descargas
cola.agregar_descarga("http://ejemplo.com/archivo1.zip", "2024-10-30","23gb")
cola.agregar_descarga("http://ejemplo.com/archivo2.zip", "2024-10-31", "44mb")

# Guardar el estado de las descargas en un archivo CSV
cola.guardar_estado_descargas()
"""