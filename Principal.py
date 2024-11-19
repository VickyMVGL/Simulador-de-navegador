import paginas
import Descargas
import Historial
import Vizualizacion
import Pestaña
from datetime import datetime

class Principal:

    def __init__(self):
        self.lista_paginas = []
        self.historial = Historial.PilaArchivos()
        self.desc = Descargas.ColaArchivos()
        
    def Abrir_txt(self):
        archivo=open(r'C:\Users\Us\Desktop\Simulador de navegador\Simulador-de-navegador\host.txt')
        print(archivo)
        lineas = archivo.readlines()
        
        for linea in lineas:
            html, ip, dominio, xx = linea.split(" ")
            pag = pagina.Pagina(html, ip, dominio)
            self.lista_paginas.append(pag)
        archivo.close()
    
    def mostrar_comandos(self):
        print("")
        print("Lista de comandos")
        print("------------------------------------")
        print("")
        print("--> ir <url o ip>: Va a una pagina")
        print("--> nueva_pestana <url o ip>: Abre una nueva pagina")
        print("--> mostrar_pestanas: Muestra las pestañas abiertas")
        print("--> cambiar_pestana: Cambia a una pestaña en especifico")
        print("--> cerrar_pestana: Cierra la pestaña actual")
        print("--> pestana_anterior: Va a la pestaña anterior a la actual")
        print("--> pestana_siguiente: Va a la pestaña siguiente a la actual")
        print("--> mostrar_historial: Muestra el historial actual")
        print("--> descargar <url>: descarga el archivo")
        print("--> mostrar_descargas: muestra las descargas")
        print("--> cancelar_descarga <n>: Cancela la descarga actual")
        print("--> listar_paginas: lista las paginas disponibles")
        print("--> mostrar_contenido_basico: Muestra el contenido en html")
        print("--> mostrar_contenido_plano: Muestra la pagina html en texto plano")
        print("--> guardar_historial: Guarda el historial en un archivo csv")
        print("--> salir: Sale del navegador")

    def leer_comando(self):
        paginas= self.lista_paginas
        
        c = input("¿Que desea realizar? (ingrese 'help' para ver la lista de comandos): ")
        
        if c == "help":
            Principal.mostrar_comandos(self)
            print("")
            print("------------------------------------------")
            print("")
            self.leer_comando()
        
        elif c.startswith("ir "):
            _, url_o_ip = c.split(" ", 1)
            
            for pagina in self.lista_paginas:
                if pagina.dominio == url_o_ip or pagina.ip == url_o_ip:
                    pagina.vizualizar()
                    fecha_actual = datetime.now().strftime("%Y-%m-%d")
                    hora_actual = datetime.now().strftime("%H:%M:%S")
                    dominio = str(url_o_ip)
                    fecha = str(fecha_actual)
                    hora = str(hora_actual)
                    self.historial.agregar_archivo(dominio, fecha, hora)
                    self.leer_comando()
                    
                    
            print("No se encontró la página.")
            self.leer_comando()

        elif c.startswith("nueva_pestana "):
            _, url_o_ip = c.split(" ", 1)
            tab = Pestaña.BrowserTabs()
            tab.open_tab(url_o_ip, url_o_ip) 
            print("")
            self.leer_comando()
            
        elif c == "mostrar_pestanas":
            tab = Pestaña.BrowserTabs()
            tab.show_tabs(self)  
            print("")
            self.leer_comando()
            
        elif c == "cambiar_pestana":
            try:
                numero = int(input("Ingrese el número de la pestaña a la que desea cambiar: "))
                tab = Pestaña.BrowserTabs()
                tab.open_a_tab(numero)
                print("")
                self.leer_comando()
            except ValueError:
                print("Por favor ingrese un número válido.")
                print("")
                self.leer_comando()


        elif c == "cerrar_pestana":
            tab = Pestaña.BrowserTabs()
            tab.close_current_tab()  
            print("")
            self.leer_comando()

        elif c == "pestana_anterior":
            tab = Pestaña.BrowserTabs()
            tab.move_to_previous_tab(self)
            print("")
            self.leer_comando()

        elif c == "pestana_siguiente":
            tab = Pestaña.BrowserTabs()
            tab.move_to_next_tab() 
            print("")
            self.leer_comando()

        elif c == "mostrar_historial":
            self.historial.mostrar_historial() 
            print("")
            self.leer_comando()
            
        elif c.startswith("descargar "):
            _, url = c.split(" ", 1)
            
            self.desc.agregar_descarga(url, "Fecha de ejemplo", "Tamaño de ejemplo") 
            print("")
            self.leer_comando()
            
        elif c == "mostrar_descargas":
            
            self.desc.mostrar_descarga()  
            self.leer_comando()

        elif c.startswith("cancelar_descarga "):
            _, n = c.split(" ", 1)
            n = int(n)
            
            for _ in range(n):
                self.desc.eliminar_descarga()
            self.leer_comando()

        elif c == "listar_paginas":
            print("")
            for pagina in self.lista_paginas:
                print(pagina.dominio)  
            print("")
            self.leer_comando()
            
        elif c == "guardar_historial":
            
            self.historial.guardar_historial(archivo_csv='historial.csv')
        
        elif c == "mostrar_contenido_basico":
            print("")
            self.leer_comando()
            pass
            
        elif c =="mostrar_contenido_plano":
            print("")
            self.leer_comando()
            pass
            
        elif c == "salir":
            print("Muchas gracias, hasta pronto!")
            return

        else:
            print("Por favor ingrese un comando valido...")
            self.leer_comando()        

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
        
p = Principal()
p.Abrir_txt()

p.leer_comando()


#"C:\\Users\\Victoria\\Desktop\\Proyectos Actuales\\Proyecto del navegador\\Simulador-de-navegador\\Assets\\host.txt", "r"