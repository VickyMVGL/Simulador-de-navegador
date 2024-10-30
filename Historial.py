class PaginaHistorial:
    def __init__(self, dominio, fecha, hora):
        self.dominio = dominio
        self.fecha = fecha
        self.hora = hora
        self.siguiente = None

class PilaArchivos:
    def __init__(self):
        self.cabeza = None
    def agregar_archivo(self, dominio, fecha, hora, ):
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
            if actual.nombre == dominio:
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
    
    def obtener_posicion(self, nombre):
        actual = self.cabeza
        pos = 0
        while actual:
            if actual.nombre == nombre:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1
    
