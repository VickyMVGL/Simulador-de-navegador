import os
from bs4 import BeautifulSoup

class Pagina:
    def __init__(self, html, ip, dominio):
        self.html = html
        self.ip = ip
        self.dominio = dominio

    def __lt__(self, other):
        return self.ip < other.ip

    def __eq__(self, other):
        return self.ip == other.ip

    def __str__(self):
        return f"IP: {self.ip}, Dominio: {self.dominio}, Html: {self.html}"

    def __repr__(self):
        return str(self)


class NTreeNode:
    def __init__(self, pagina=None):
        self.pagina = pagina
        self.children = []

    def insert(self, pagina):
        self.children.append(NTreeNode(pagina))

    def __str__(self):
        return str(self.pagina)


class NTree:
    def __init__(self):
        self.root = None

    def Abrir_txt(self):
        archivo=open(r'host.txt')
        print(archivo)
        lineas = archivo.readlines()
        lista_paginas = []
        
        for linea in lineas:
            html, ip, dominio, xx = linea.split(" ")
            pag = Pagina(html, ip, dominio)
            lista_paginas.append(pag)

        archivo.close()

        return lista_paginas

    def insert(self, pagina):
        if not self.root:
            self.root = NTreeNode(pagina)
        else:
            self._insert_recursive(self.root, pagina)

    def _insert_recursive(self, node, pagina):
        if not node.children:
            node.insert(pagina)
        else:
            for child in node.children:
                self._insert_recursive(child, pagina)

    def traverse(self):
        if self.root:
            self._traverse_recursive(self.root)

    def _traverse_recursive(self, node):
        print(node)
        for child in node.children:
            self._traverse_recursive(child)

    def inorden(self):
        if self.root:
            self._inorden_recursive(self.root)

    def _inorden_recursive(self, node):
        if node:
            for child in node.children:
                self._inorden_recursive(child)
            print(node)
    
    def _inorden_recursive_search(self, node):
        if node:
            for child in node.children:
                self._inorden_recursive(child)
            print(self.pagina.dominio)

    def postorden(self):
        if self.root:
            self._postorden_recursive(self.root)

    def _postorden_recursive(self, node):
        if node:
            for child in node.children:
                self._postorden_recursive(child)
            print(node)
    
    def _postorden_recursive(self, node):
        if node:
            for child in node.children:
                
                self._postorden_recursive(child)
            print(node)

#Hacer una funcion que devuelva segun el nombre

    def _postorden_recursive_search(self, node, dominio):
            node= self.root
            if node:
                for child in node.children:
                    if self.root.producto.dominio == dominio:
                        return node
                    self._postorden_recursive(child) 
            return None
"""
    def ir(self, paginas,  dominio):
        
        lista_paginas = paginas
        for pagina in lista_paginas:
            try:
                with open(nodo.ruta_archivo, 'r', encoding='utf-8') as archivo:
                    print(f"Mostrando contenido de '{nodo.name}' ({nodo.ip}):\n")
                    print(archivo.read())
                return
            except Exception as e:
                print(f"Error al abrir el archivo '{nodo.ruta_archivo}': {e}")
                return
            """

    


# Ejemplo de uso:
n_tree = NTree()

# Crear e insertar productos
paginas = n_tree.Abrir_txt()
for pagina in paginas:
    n_tree.insert(pagina)

# Recorrer el árbol en inorden
print("\nInorden traversal of the constructed N-tree with Productos is:")

n_tree.inorden()

print("_____________________-")
n_tree.ir(paginas, "www.youtube.com")

"""

print("\nBuscar producto:")
n_tree._postorden_recursive_search(None, "Producto H")
"""