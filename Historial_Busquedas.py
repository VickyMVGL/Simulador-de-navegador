from datetime import datetime

class NodoBusqueda:
    def __init__(self, clave, fecha_hora):
        self.clave = clave
        self.fecha_hora = fecha_hora
        self.izquierda = None
        self.derecha = None

class HistorialABB:
    def __init__(self):
        self.raiz = None
        self.archivo_csv = "busquedas.csv"
        self.cargar_desde_csv()

    def insertar(self, clave, fecha_hora=None):
        if fecha_hora is None:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.raiz = self._insertar_nodo(self.raiz, clave, fecha_hora)
        self.guardar_en_csv(clave, fecha_hora)

    def _insertar_nodo(self, nodo, clave, fecha_hora):
        if nodo is None:
            return NodoBusqueda(clave, fecha_hora)
        if clave < nodo.clave:
            nodo.izquierda = self._insertar_nodo(nodo.izquierda, clave, fecha_hora)
        else:
            nodo.derecha = self._insertar_nodo(nodo.derecha, clave, fecha_hora)
        return nodo

    def buscar(self, clave):
        resultados = []
        self._buscar_nodo(self.raiz, clave, resultados)
        return resultados

    def _buscar_nodo(self, nodo, clave, resultados):
        if nodo is not None:
            if clave in nodo.clave:
                resultados.append((nodo.clave, nodo.fecha_hora))
            self._buscar_nodo(nodo.izquierda, clave, resultados)
            self._buscar_nodo(nodo.derecha, clave, resultados)

    def mostrar_historial(self):
        historial = []
        self._inorden(self.raiz, historial)
        return historial

    def _inorden(self, nodo, historial):
        if nodo is not None:
            self._inorden(nodo.izquierda, historial)
            historial.append((nodo.clave, nodo.fecha_hora))
            self._inorden(nodo.derecha, historial)

    def eliminar_por_clave(self, clave):
        self.raiz = self._eliminar_nodo(self.raiz, clave)
        self.actualizar_csv()

    def eliminar_por_fecha(self, fecha_limite):
        fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")
        self.raiz = self._eliminar_por_fecha(self.raiz, fecha_limite)
        self.actualizar_csv()

    def _eliminar_nodo(self, nodo, clave):
        if nodo is None:
            return None
        if clave in nodo.clave:
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            min_larger_node = self._encontrar_minimo(nodo.derecha)
            nodo.clave, nodo.fecha_hora = min_larger_node.clave, min_larger_node.fecha_hora
            nodo.derecha = self._eliminar_nodo(nodo.derecha, min_larger_node.clave)
        elif clave < nodo.clave:
            nodo.izquierda = self._eliminar_nodo(nodo.izquierda, clave)
        else:
            nodo.derecha = self._eliminar_nodo(nodo.derecha, clave)
        return nodo

    def _eliminar_por_fecha(self, nodo, fecha_limite):
        if nodo is None:
            return None
        nodo.izquierda = self._eliminar_por_fecha(nodo.izquierda, fecha_limite)
        nodo.derecha = self._eliminar_por_fecha(nodo.derecha, fecha_limite)
        fecha_nodo = datetime.strptime(nodo.fecha_hora, "%Y-%m-%d %H:%M:%S")
        if fecha_nodo > fecha_limite:
            return self._eliminar_nodo(nodo, nodo.clave)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def guardar_en_csv(self, clave, fecha_hora):
        with open(self.archivo_csv, mode="a", encoding="utf-8") as archivo:
            archivo.write(f"{clave},{fecha_hora}\n")

    def cargar_desde_csv(self):
        try:
            with open(self.archivo_csv, mode="r", encoding="utf-8") as archivo:
                for linea in archivo:
                    clave, fecha_hora = linea.strip().split(",", 1)
                    self.raiz = self._insertar_nodo(self.raiz, clave, fecha_hora)
        except FileNotFoundError:
            pass

    def actualizar_csv(self):
        historial = self.mostrar_historial()
        with open(self.archivo_csv, mode="w", encoding="utf-8") as archivo:
            for clave, fecha_hora in historial:
                archivo.write(f"{clave},{fecha_hora}\n")


"""
# Ejemplo de uso
if __name__ == "__main__":
    historial = HistorialABB()

    # Insertar búsquedas
    historial.insertar("python tutorial")
    historial.insertar("árboles binarios")
    historial.insertar("estructuras de datos")

    # Buscar
    print("Búsqueda de 'python':", historial.buscar("python"))

    # Mostrar historial completo
    print("Historial completo:", historial.mostrar_historial())

    # Eliminar por clave
    historial.eliminar_por_clave("python")
    print("Historial después de eliminar 'python':", historial.mostrar_historial())

    # Eliminar por fecha
    historial.eliminar_por_fecha("2024-01-01")
    print("Historial después de eliminar por fecha:", historial.mostrar_historial())
"""