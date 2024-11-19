class PaginaHistorial:
    def __init__(self, dominio, fecha, hora):
        self.dominio = dominio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None

class PilaArchivos:
    def __init__(self):
        self.cabeza = None
        
    def agregar_archivo(self, dominio, fecha, hora):
        nuevo_nodo = PaginaHistorial(dominio, fecha, hora)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def mostrar_historial(self):
        actual = self.cabeza
        while actual:
            print("Dominio: ", actual.dominio)
            print("Fecha: ", actual.fecha)
            print("Hora: ", actual.hora)
            print("------------------------------------------")
            actual = actual.siguiente

    def buscar_archivo(self, dominio):
        actual = self.cabeza
        while actual:
            if actual.dominio == dominio:
                return True
            actual = actual.siguiente
        return False
    
    def eliminar_archivo(self):
        if not self.cabeza:
            return None
        eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return eliminado
    
    def modificar_archivo(self, dominio, nuevo_dominio, fecha, hora):
        actual = self.cabeza
        while actual:
            if actual.dominio == dominio:
                actual.dominio = nuevo_dominio
                actual.fecha= fecha
                actual.hora = hora
                return True
            actual = actual.siguiente
        return False
    
    def obtener_posicion(self, dominio):
        actual = self.cabeza
        pos = 0
        while actual:
            if actual.dominio == dominio:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1
    
    def guardar_historial(self, archivo_csv='historial.csv'):
        with open(archivo_csv, 'w') as file:
            file.write("Dominio,Fecha,Hora\n")
            actual = self.cabeza
            while actual:
                file.write(f"{actual.dominio},{actual.fecha},{actual.hora}\n")
                actual = actual.siguiente
        print(f"Historial guardado en {archivo_csv}.")


"""
#Pruebas

pila = PilaArchivos()

# Agregar páginas al historial
pila.agregar_archivo("193.568.089", "2024-10-30", "10:00")
pila.agregar_archivo("www.otroejemplo.com", "2024-10-31", "12:00")

# Mostrar el historial
pila.mostrar_historial()

# Guardar el historial en un archivo CSV
pila.guardar_historial()
"""