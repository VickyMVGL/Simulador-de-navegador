from datetime import datetime
import csv


class NodoPagina:
    def __init__(self, id, html, ip, dominio, nombre_sitio):
        self.id = id
        self.html = html
        self.ip = ip
        self.dominio = dominio
        self.nombre_sitio = nombre_sitio
        self.fecha_agregado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

    def agregar(self, nodo, id, html, ip, dominio, nombre_sitio):
        if not nodo:
            return NodoPagina(id, html, ip, dominio, nombre_sitio)
        if id < nodo.id:
            nodo.izquierda = self.agregar(nodo.izquierda, id, html, ip, dominio, nombre_sitio)
        elif id > nodo.id:
            nodo.derecha = self.agregar(nodo.derecha,id, html, ip, dominio, nombre_sitio)
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
        
        self.exportar_favoritos_a_csv("favoritos.csv")
        return nodo

    def agregar_favorito(self,  id, html, ip, dominio, nombre_sitio):
        self.raiz = self.agregar(self.raiz, id, html, ip, dominio, nombre_sitio)
    
    def obtener_minimo(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def eliminar(self, nodo,  id, html, ip, dominio, nombre_sitio):
        #Esta va a ser la parte de eliminar
        if not nodo:
            return nodo

        # Buscar el nodo a eliminar
        if id < nodo.id:
            nodo.izquierda = self.eliminar(nodo.izquierda,  id, html, ip, dominio, nombre_sitio)
        elif id > nodo.id:
            nodo.derecha = self.eliminar(nodo.derecha, id, html, ip, dominio, nombre_sitio)
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
            nodo.derecha = self.eliminar(nodo.derecha, temp.id, temp.html, temp.ip, temp.dominio, temp.nombre_sitio)
            
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
        
        self.exportar_favoritos_a_csv("favoritos.csv")
        return nodo

    def eliminar_favorito(self,  id, html, ip, dominio, nombre_sitio):
        self.raiz = self.eliminar(self.raiz, id, html, ip, dominio, nombre_sitio)


    
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
                "dominio": nodo.dominio,
                "nombre del sitio": nodo.nombre_sitio,
                "fecha agregado": nodo.fecha_agregado
                })
            

        return resultado

    def mostrar_favoritos(self):
        return self.buscar_postorden(self.raiz)

    def buscar_preorden(self, nodo, domOrIp):
        if not nodo:
            return None  # Si el nodo es nulo, no hay nada que buscar

        # Verificar si el nodo actual tiene el ID buscado
        if nodo.dominio == domOrIp or nodo.ip == domOrIp:
            return {
                "id": nodo.id,
                "html": nodo.html,
                "ip": nodo.ip,
                "dominio": nodo.dominio,
                "nombre del sitio": nodo.nombre_sitio,
                "fecha agregado": nodo.fecha_agregado
            }


        # Buscar en el subárbol izquierdo
        resultado_izquierda = self.buscar_preorden(nodo.izquierda, domOrIp)
        if resultado_izquierda:
            return resultado_izquierda
        # Buscar en el subárbol derecho
        return self.buscar_preorden(nodo.derecha, domOrIp)

    def buscar_favorito(self, domOrIp):
        resultado = self.buscar_preorden(self.raiz, domOrIp)
        if resultado:
            print(f"Favorito encontrado: {resultado}")
        else:
            print(f"No se encontró un favorito: {domOrIp}")    
    
    def guardar_favoritos_en_csv(self, archivo_csv):
        favoritos = self.buscar_postorden(self.raiz)  # Obtenemos todos los favoritos en preorden
        if not favoritos:
            print("No hay favoritos para guardar.")
            return

        # Escribimos los datos en un archivo CSV
        with open(archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            # Encabezados
            escritor.writerow(["ID", "Nombre del Sitio", "HTML", "IP", "Dominio", "Fecha Agregado"])
            # Datos
            for favorito in favoritos:
                escritor.writerow([
                    favorito["id"],
                    favorito["nombre del sitio"],
                    favorito["html"],
                    favorito["ip"],
                    favorito["dominio"],
                    favorito["fecha agregado"]
                ])
        print(f"Favoritos guardados exitosamente en {archivo_csv}.")
    
    def exportar_favoritos_a_csv(self, archivo_csv="favoritos.csv"):
        self.guardar_favoritos_en_csv(archivo_csv)
            
# Ejemplo de uso
fs = AVLFileSystem()
fs.agregar_favorito(10, "<html1>", "192.168.1.1", "example.com", "example")
fs.agregar_favorito(5, "<html2>", "192.168.1.2", "example2.com", "example")
fs.agregar_favorito(15, "<html3>", "192.168.1.3", "example3.com", "example")
fs.agregar_favorito(3, "<html4>", "192.168.1.4", "example4.com", "example")
fs.agregar_favorito(7, "<html5>", "192.168.1.5", "example5.com", "example")
fs.agregar_favorito(20, "<html6>", "192.168.1.6", "example6.com", "example")
print("_________________________________")
# Buscar favoritos en preorden
favoritos = fs.mostrar_favoritos()
print(favoritos)
print("_____________")

fs.buscar_favorito("192.168.1.6")  # Favorito con ID 7
fs.buscar_favorito("192.168.1.8")  # ID que no existe