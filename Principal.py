import pagina, Descargas, Historial, Vizualizacion, Pestaña, Historial_Busquedas, Cache
from datetime import datetime

class Principal:

    def __init__(self):
        self.lista_paginas = []
        self.historial = Historial.PilaArchivos()
        self.desc = Descargas.ColaArchivos()
        self.hist_busqueda = Historial_Busquedas.HistorialABB()
        self.cache = Cache.Cache()
        self.tab = Pestaña.BrowserTabs()

    def Abrir_txt(self):
        archivo=open(r'host.txt')
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
        print("--> mostrar_paginas: lista las paginas segun jerarquia (Arbol N-Ario)")
        print("--> ir_a_pagina <url o ip>: muestra el archivo html en el arbol de archivos locales y mostrara el contenido")
        print("--> mostrar_contenido_basico: Muestra el contenido en html")
        print("--> mostrar_contenido_plano: Muestra la pagina html en texto plano")
        print("--> guardar_historial: Guarda el historial en un archivo csv")
        print("--> buscar <palabra_clave>: Realiza una búsqueda de palabras clave en el historial de búsquedas")
        print("--> mostrar_historial_busquedas: Muestra todas las búsquedas almacenadas en orden")
        print("--> eliminar_busqueda_key")
        print("--> eliminar_busqueda_fecha")            
        print("--> agregar_cache")           
        print("--> obtener_cache")           
        print("--> vaciar_cache")
        print("--> salir: Sale del navegador")


    def leer_comando(self):
        
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
            dominio = str(url_o_ip)
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            hora_actual = datetime.now().strftime("%H:%M:%S")
            fecha = str(fecha_actual)
            hora = str(hora_actual)
            self.tab.open_tab(url_o_ip, url_o_ip) 
            self.historial.agregar_archivo(dominio, fecha, hora)
            print("")
            self.leer_comando()

        elif c == "mostrar_pestanas":
            
            self.tab.show_tabs()  
            print("")
            self.leer_comando()

        elif c == "cambiar_pestana":
            try:
                numero = int(input("Ingrese el número de la pestaña a la que desea cambiar: "))
                self.tab.open_a_tab(numero)
                print("")
                self.leer_comando()
            except ValueError:
                print("Por favor ingrese un número válido.")
                print("")
                self.leer_comando()

        elif c == "cerrar_pestana":
            self.tab.close_current_tab()  
            print("")
            self.leer_comando()

        elif c == "pestana_anterior":
            self.tab.move_to_previous_tab()
            print("")
            self.leer_comando()

        elif c == "pestana_siguiente":
            self.tab.move_to_next_tab() 
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
            self.leer_comando()

        elif c == "mostrar_contenido_basico":
            print("")
            self.leer_comando()
            pass

        elif c =="mostrar_contenido_plano":
            print("")
            self.leer_comando()
            pass

        elif c.startswith("buscar"):
            self.hist_busqueda.buscar()
            self.leer_comando()
            
            

        elif c == "mostrar_historial_busquedas":
            self.hist_busqueda.mostrar_historial()
            self.leer_comando()

        elif c.startswith("eliminar_busqueda_key"):
            _, n =c.split(" ",1)
            self.hist_busqueda.eliminar_por_clave(n)
            self.leer_comando()
            
        
        elif c.startswith("eliminar_busqueda_fecha"):
            _, n =c.split(" ",1)
            self.hist_busqueda.eliminar_por_fecha(n)
            self.leer_comando()
            

        elif c.startswith("agregar_cache"):
            self.leer_comando()

        elif c.startswith("obtener_cache"):
            self.leer_comando()

        elif c.startswith("vaciar_cache"):
            self.leer_comando()

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