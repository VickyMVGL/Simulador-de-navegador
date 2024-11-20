import os
from bs4 import BeautifulSoup

class SimuladorNavegador:
    def __init__(self, carpeta_simulada="paginas_simuladas"):
        self.carpeta_simulada = carpeta_simulada
        self.archivo_actual = None
        self.contenido_actual = None

        # Crear la carpeta simulada si no existe
        if not os.path.exists(self.carpeta_simulada):
            os.makedirs(self.carpeta_simulada)

    def listar_paginas(self):
        """Lista todas las páginas .html disponibles en la carpeta simulada."""
        paginas = [archivo for archivo in os.listdir(self.carpeta_simulada) if archivo.endswith(".html")]
        if paginas:
            print("Páginas disponibles:")
            for pagina in paginas:
                print(f"- {pagina}")
        else:
            print("No hay páginas disponibles.")

    def ir(self, direccion):
        """Visita una página simulada cargando su contenido desde un archivo .html."""
        paginas = self.listar_paginas()
        if direccion not in paginas:
            print(f"La página '{direccion}' no está registrada en el archivo de índice.")
            return

        archivo_path = os.path.join(self.carpeta_simulada, direccion)
        if os.path.isfile(archivo_path) and archivo_path.endswith(".html"):
            try:
                with open(archivo_path, 'r', encoding='utf-8') as archivo:
                    self.contenido_actual = archivo.read()
                self.archivo_actual = direccion
                print(f"Página '{direccion}' cargada exitosamente.")
            except Exception as e:
                print(f"Error al cargar la página '{direccion}': {e}")
        else:
            print(f"La página '{direccion}' no existe o no es un archivo .html válido.")

    def mostrar_contenido(self, modo="basico"):
        """Muestra el contenido de la página actual en el modo especificado."""
        if not self.contenido_actual:
            print("No se ha cargado ninguna página. Use el comando 'ir <url o ip>' primero.")
            return

        if modo == "basico":
            print("Modo Básico: Mostrando el código HTML sin procesar.")
            print(self.contenido_actual)
        elif modo == "texto_plano":
            print("Modo Texto Plano: Mostrando solo el texto sin etiquetas HTML.")
            soup = BeautifulSoup(self.contenido_actual, 'html.parser')
            print(soup.get_text())
        else:
            print(f"Modo '{modo}' no reconocido. Use 'basico' o 'texto_plano'.")

# Ejemplo de uso
if __name__ == "__main__":
    navegador = SimuladorNavegador()

    while True:
        try:
            comando = input("\n> ").strip().lower()
            
            if not comando:
                print("Por favor, ingresa un comando válido.")
                continue

            if comando == "listar_paginas":
                print("Listando páginas...")  # Aquí llamas a la función correspondiente
            elif comando.startswith("ir "):
                partes = comando.split(" ", 1)
                if len(partes) > 1:
                    direccion = partes[1]
                    print(f"Visitando la página: {direccion}")
                    # Aquí llamas a la función correspondiente
                else:
                    print("Error: falta la dirección en el comando 'ir'.")
            elif comando.startswith("mostrar_contenido "):
                partes = comando.split(" ", 1)
                if len(partes) > 1:
                    modo = partes[1]
                    if modo in ["basico", "texto_plano"]:
                        print(f"Mostrando contenido en modo: {modo}")
                        # Aquí llamas a la función correspondiente
                    else:
                        print("Modo no válido. Use 'basico' o 'texto_plano'.")
                else:
                    print("Error: falta el modo en el comando 'mostrar_contenido'.")
            elif comando == "salir":
                print("Saliendo del simulador de navegador.")
                break
            else:
                print("Comando no reconocido. Intenta de nuevo.")

        except KeyboardInterrupt:
            print("\nInterrupción detectada. Use 'salir' para terminar el programa.")
        except Exception as e:
            print(f"Se produjo un error: {e}")