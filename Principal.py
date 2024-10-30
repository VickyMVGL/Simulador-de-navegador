import pagina
import Descargas
import Historial
import Vizualizacion
import Pestaña
from datetime import datetime

class Principal:

    def __init__(self):
        self.lista_paginas = []
        
    def Abrir_txt(self):
        archivo=open(r'C:\Users\Manuel Hernandez\Documents\UJAP\Algoritmos 2\Simulador-de-navegador\host.txt')
        print(archivo)
        lineas = archivo.readlines()
        
        for linea in lineas:
            html, ip, dominio = linea.split(" ")
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
                    historial = Historial.PilaArchivos()
                    historial.agregar_archivo(url_o_ip, fecha_actual, hora_actual)
                    self.leer_comando()
                    return
            print("No se encontró la página.")
            self.leer_comando()

        elif c.startswith("nueva_pestana "):
            _, url_o_ip = c.split(" ", 1)
            Pestaña.BrowserTabs.open_tab(url_o_ip, url_o_ip)  # Llama al método para abrir una nueva pestaña
            print("")
            self.leer_comando()
            
        elif c == "mostrar_pestanas":
            Pestaña.BrowserTabs.show_tabs(self)  # Llama al método para mostrar las pestañas abiertas
            print("")
            self.leer_comando()
            
        elif c == "cambiar_pestana":
            try:
                numero = int(input("Ingrese el número de la pestaña a la que desea cambiar: "))
                Pestaña.BrowserTabs.open_a_tab(numero)
                print("")
                self.leer_comando()
            except ValueError:
                print("Por favor ingrese un número válido.")
                print("")
                self.leer_comando()


        elif c == "cerrar_pestana":
            Pestaña.BrowserTabs.close_current_tab()  
            print("")
            self.leer_comando()

        elif c == "pestana_anterior":
            Pestaña.BrowserTabs.move_to_previous_tab(self)
            print("")
            self.leer_comando()

        elif c == "pestana_siguiente":
            Pestaña.BrowserTabs.move_to_next_tab() 
            print("")
            self.leer_comando()

        elif c == "mostrar_historial":
            historial = Historial.PilaArchivos()
            historial.mostrar_historial() 
            print("")
            self.leer_comando()
            
        elif c.startswith("descargar "):
            _, url = c.split(" ", 1)
            Descargas.ColaArchivos.agregar_archivo(url, "Fecha de ejemplo", "Tamaño de ejemplo") 
            print("")
            self.leer_comando()
            
        elif c == "mostrar_descargas":
            Descargas.ColaArchivos.mostrar_archivos()  

        elif c.startswith("cancelar_descarga "):
            _, n = c.split(" ", 1)
            n = int(n)
            for _ in range(n):
                Descargas.ColaArchivos.eliminar_archivo()  

        elif c == "listar_paginas":
            print("")
            for pagina in self.lista_paginas:
                print(pagina.dominio)  
            print("")
            self.leer_comando()
            
        elif c == "guardar_historial":
            historial = Historial.PilaArchivos()
            historial.guardar_historial(archivo_csv='historial.csv')
        
            
        elif c == "salir":
            print("Muchas gracias, hasta pronto!")
            return

        else:
            print("Por favor ingrese un comando valido...")
            self.leer_comando()        


p = Principal()
p.Abrir_txt()

p.leer_comando()


#"C:\\Users\\Victoria\\Desktop\\Proyectos Actuales\\Proyecto del navegador\\Simulador-de-navegador\\Assets\\host.txt", "r"

"""
    def leer_comando(self, comando):
        paginas= self.lista_paginas
        c, control = comando.split(" ")

        elif c == "guardar_historial":
            if Historial.PilaArchivos.cabeza != "null":
                Historial.PilaArchivos.agregar_archivo(self)
                Historial.PilaArchivos.guardar_historial(self)
                self.leer_comando()
                
            else:
                print("No hay nada que guardar...")
                self.leer_comando()
                
                
        elif c == "ir":
            for pagina in paginas:
                #if control == pagina.dominio:
                    pagina.vizualizar()
                    break
                #else:
                    pass
                


"""