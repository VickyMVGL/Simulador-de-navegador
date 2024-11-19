class NodoPagina:
    def __init__(self, id, , monto, dir_facturacion, dir_envio):
        self.id = id
        self.descripcion = descripcion
        self.monto = monto
        self.dir_facturacion = dir_facturacion
        self.dir_envio = dir_envio 
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

    def insertar(self, nodo, id, descripcion, monto, dir_facturacion, dir_envio):
        if not nodo:
            return NodoArchivo(id,  descripcion, monto, dir_facturacion, dir_envio)

        if id < nodo.id:
            nodo.izquierda = self.insertar(nodo.izquierda, id,  descripcion, monto, dir_facturacion, dir_envio)
        elif id > nodo.id:
            nodo.derecha = self.insertar(nodo.derecha, id, descripcion, monto, dir_facturacion, dir_envio)
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

    def insertar_archivo(self, id,  descripcion, monto, dir_facturacion, dir_envio):
        self.raiz = self.insertar(self.raiz, id,  descripcion, monto, dir_facturacion, dir_envio)


    def preorden(self, nodo):
        print(nodo.id)
        print(nodo.descripcion)
        if nodo.izquierda != None:
            self.preorden(nodo.izquierda)
        if nodo.derecha != None:
            
            self.preorden(nodo.derecha)
        
            
# Ejemplo de uso
avl_fs = AVLFileSystem()
avl_fs.insertar_archivo("1", "p1", 123, "SD", "Ca")
avl_fs.insertar_archivo("2", "p2", 150, "CA", "CSS")
avl_fs.insertar_archivo("3", "p3", 100, "Sd", "Css")

avl_fs.preorden(avl_fs.raiz)