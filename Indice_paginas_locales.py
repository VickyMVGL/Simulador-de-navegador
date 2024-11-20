import os
from anytree import Node, RenderTree, PreOrderIter

class ArbolNarioPaginas:
    def __init__(self, archivo_host, carpeta_simulada):
        self.archivo_host = archivo_host
        self.carpeta_simulada = carpeta_simulada
        self.raiz = Node("Raíz")
        self.cargar_host()

    def cargar_host(self):
        """
        Carga la estructura del archivo host.txt en el árbol N-ario.
        El archivo debe tener líneas con formato: URL/IP, ruta del archivo.
        Ejemplo:
        192.168.102,www.google.com,google.html
        """
        if not os.path.isfile(self.archivo_host):
            print(f"El archivo host '{self.archivo_host}' no existe.")
            return
        
        try:
            with open(self.archivo_host, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split(',')
                    if len(partes) == 3:
                        ip, url, ruta = partes
                        ruta_absoluta = os.path.join(self.carpeta_simulada, ruta)
                        if os.path.isfile(ruta_absoluta):
                            # Construir nodos jerárquicos
                            segmentos = url.split('.')
                            nodo_actual = self.raiz
                            for segmento in reversed(segmentos):
                                hijo_existente = next((n for n in nodo_actual.children if n.name == segmento), None)
                                if not hijo_existente:
                                    hijo_existente = Node(segmento, parent=nodo_actual)
                                nodo_actual = hijo_existente
                            Node(ruta, parent=nodo_actual, ip=ip, ruta_archivo=ruta_absoluta)
        except Exception as e:
            print(f"Error al cargar el archivo host: {e}")

    def listar_paginas(self):
        """Muestra todas las páginas disponibles recorriendo el árbol N-ario."""
        print("Estructura de páginas disponibles:")
        for pre, _, node in RenderTree(self.raiz):
            if 'ruta_archivo' in node.__dict__:  # Nodo hoja (archivo HTML)
                print(f"{pre}{node.name} (Archivo: {node.ruta_archivo}, IP: {node.ip})")
            else:
                print(f"{pre}{node.name}")

    def ir(self, direccion):
        """Busca y muestra el contenido del archivo HTML desde su URL o IP."""
        for node in PreOrderIter(self.raiz):
            if 'ruta_archivo' in node.__dict__ and (node.name == direccion or node.ip == direccion):
                try:
                    with open(node.ruta_archivo, 'r', encoding='utf-8') as archivo:
                        print(f"Mostrando contenido de '{node.name}' ({node.ip}):")
                        print(archivo.read())
                        return
                except Exception as e:
                    print(f"Error al cargar el archivo '{node.ruta_archivo}': {e}")
                    return
        print(f"No se encontró ninguna página con la dirección '{direccion}'.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Supongamos que los archivos están en la carpeta 'paginas_simuladas'
    carpeta_simulada = "paginas_simuladas"
    archivo_host = "host.txt"

    navegador = ArbolNarioPaginas(archivo_host, carpeta_simulada)
    
    # Listar las páginas
    navegador.listar_paginas()
    
    # Acceder a una página
    navegador.ir("www.google.com")
    navegador.ir("192.168.102")