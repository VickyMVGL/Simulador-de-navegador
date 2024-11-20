class NodoPagina:
    def __init__(self, id, html, ip, dominio):
        self.id = id
        self.html = html
        self.ip = ip
        self.dominio = dominio
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVLFileSystem:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def agregar(self, nodo, id, html, ip, dominio):
        if not nodo:
            return NodoPagina(id, html, ip, dominio)
        if id < nodo.id:
            nodo.izquierda = self.agregar(nodo.izquierda, id, html, ip, dominio)
        elif id > nodo.id:
            nodo.derecha = self.agregar(nodo.derecha,id, html, ip, dominio)
        else:
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_balance(nodo)

        if balance > 1 and id < nodo.izquierda.id:
            return self.rotar_derecha(nodo)

        if balance < -1 and id > nodo.derecha.id:
            return self.rotar_izquierda(nodo)

        if balance > 1 and id > nodo.izquierda.id:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if balance < -1 and id < nodo.derecha.id:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def agregar_favorito(self, id, html, ip, dominio):
        self.raiz = self.agregar(self.raiz, id, html, ip, dominio)
    
    def obtener_minimo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def eliminar(self, nodo, id, html, ip, dominio):
        #Esta va a ser la parte de eliminar
        if not nodo:
            return nodo

        # Buscar el nodo a eliminar
        if id < nodo.id:
            nodo.izquierda = self.eliminar(nodo.izquierda, id, html, ip, dominio)
        elif id > nodo.id:
            nodo.derecha = self.eliminar(nodo.derecha, id, html, ip, dominio)
        else:
            # Caso 1: Nodo con uno o ningún hijo
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
        
            # Caso 2: Nodo con dos hijos
            temp = self.obtener_minimo(nodo.derecha)
            nodo.id = temp.id
            nodo.html = temp.html
            nodo.ip = temp.ip
            nodo.dominio = temp.dominio
            nodo.derecha = self.eliminar(nodo.derecha, temp.id, temp.html, temp.ip, temp.dominio)
            
        #Esta es la parte que balancea el arbol

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        balance = self.obtener_balance(nodo)

        if balance > 1 and id < nodo.izquierda.id:
            return self.rotar_derecha(nodo)

        if balance < -1 and id > nodo.derecha.id:
            return self.rotar_izquierda(nodo)

        if balance > 1 and id > nodo.izquierda.id:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)

        if balance < -1 and id < nodo.derecha.id:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def eliminar_favorito(self, id, html, ip, dominio):
        self.raiz = self.eliminar(self.raiz, id, html, ip, dominio)

        
    
    def buscar_postorden(self, nodo, resultado=None):
        if resultado is None:
            resultado = []  # Inicializa la lista de resultados solo una vez
        
        if nodo:
            # Recorrer el subárbol izquierdo
            self.buscar_postorden(nodo.izquierda, resultado)
            # Recorrer el subárbol derecho
            self.buscar_postorden(nodo.derecha, resultado)
            # Añadir el nodo actual a los resultados
            resultado.append({
                "id": nodo.id,
                "html": nodo.html,
                "ip": nodo.ip,
                "dominio": nodo.dominio
            })

        return resultado

    def mostrar_favoritos(self):
        return self.buscar_postorden(self.raiz)
            
            
# Ejemplo de uso
fs = AVLFileSystem()
fs.agregar_favorito(10, "<html1>", "192.168.1.1", "example.com")
fs.agregar_favorito(5, "<html2>", "192.168.1.2", "example2.com")
fs.agregar_favorito(15, "<html3>", "192.168.1.3", "example3.com")
fs.agregar_favorito(3, "<html4>", "192.168.1.4", "example4.com")
fs.agregar_favorito(7, "<html5>", "192.168.1.5", "example5.com")
fs.agregar_favorito(20, "<html6>", "192.168.1.6", "example6.com")
print("_________________________________")
# Buscar favoritos en preorden
favoritos = fs.obtener_favoritos_preorden()
print(favoritos)