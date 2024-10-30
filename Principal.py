import pagina

class Principal:

    def __init__(self):
        lista_paginas = []
        
    def Abrir_txt(self):
        archivo=open("C:\\Users\\Victoria\\Desktop\\Proyectos Actuales\\Proyecto del navegador\\Simulador-de-navegador\\Assets\\host.txt", "r")
        print(archivo)
        lineas = archivo.readlines()
        
        for linea in lineas:
            html, ip, dominio = linea.split(" ")
            pag = pagina.Pagina(html, ip, dominio)
            self.lista_paginas.append(pag)
            
        archivo.close()
    
    def mostrar_comandos(self):
        print("Lista de comandos")
        print("------------------------------------")
        print("--> ir: Va a una pagina")
        print("--> nueva_pestana: Abre una nueva pagina")
        print("--> mostrar_pestanas: Muestra las pestañas abiertas")
        print("--> cambiar_pestana: Cambia a una pestana en especifico")
        print("--> cerrar_pestana: Cierra la pestaña actual")
        print("--> pestana_anterior: Va a la pestaña anterior a la actual")
        print("--> pestana_siguiente: Va a la pestaña siguiente a la actual")
        print("--> mostrar_historial: Muestra el historial actual")
        print("--> descargar: descarga el archivo")
        print("--> mostrar_descargas: muestra las descargas")
        print("--> cancelar_descarga: Cancela la descarga actual")
        print("--> listar_paginas: lista las paginas disponibles")
        print("--> mostrar_contenido_basico: Muestra el contenido en html")
        print("--> mostrar_contenido_plano: Muestra la pagina html en texto plano")
        print("--> guardar_historial: Guarda el historial en un archivo csv")
        print("--> salir: Sale del navegador")

        def leer_comando(self, comando):
            paginas= self.lista_paginas
            c, control = comando.split(" ")
            if c == "ir":
                for pagina in paginas:
                    if control == pagina.dominio:
                        pagina.vizualizar()
                        break
                    else:
                        pass
                





p = Principal()
p.Abrir_txt()