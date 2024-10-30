class Tab:
    def __init__(self, url, title, load_time=0):
        self.url = url
        self.title = title
        self.load_time = load_time  # Tiempo de carga de la página
        self.is_active = False  # Pestaña activa
        self.history = [url]  # Historial de URLs visitadas en la pestaña
        self.next = None  # Siguiente pestaña
        self.prev = None  # Pestaña anterior

    def visit_url(self, new_url):
        """Visitar una nueva URL en esta pestaña, actualizando el historial."""
        self.history.append(new_url)
        self.url = new_url

    def show_info(self):
        """Muestra la información detallada de la pestaña."""
        status = " (Activa)" if self.is_active else ""
        print("Pestaña: " + self.title + " URL: " + self.url + " Tiempo de carga: " + str(self.load_time) + "seg ")
        print("Historial: "+ self.history[0])

class BrowserTabs:
    def __init__(self):
        self.current_tab = None

    def open_tab(self, url, title, load_time=0):
        new_tab = Tab(url, title, load_time)
        if not self.current_tab:
            self.current_tab = new_tab
            self.current_tab.is_active = True  # La primera pestaña abierta es la activa
        else:
            temp = self.current_tab
            while temp.next:  # Vamos al final de la lista
                temp = temp.next
            temp.next = new_tab
            new_tab.prev = temp

    def open_a_tab(self, numero):
        if numero > len(self.history):
            print("No existe esa pestaña")
        else:
            temp = self.current_tab
            cont = 0
            while cont < numero:  # Vamos al final de la lista
                temp = temp.next
                cont += 1
            temp.show_info()

    def show_tabs(self):
        temp = self.current_tab
        while temp:
            temp.show_info()  #Mostrar información detallada de cada pestaña
            temp = temp.next

    def move_to_next_tab(self):
        if self.current_tab and self.current_tab.next:
            self.current_tab.is_active = False  # Desactivar la pestaña actual
            self.current_tab = self.current_tab.next
            self.current_tab.is_active = True  # Activar la siguiente pestaña
            print("Movido a: " + self.current_tab.title)
        else:
            print("No hay más pestañas.")

    def move_to_previous_tab(self):
        if self.current_tab and self.current_tab.prev:
            self.current_tab.is_active = False  # Desactivar la pestaña actual
            self.current_tab = self.current_tab.prev
            self.current_tab.is_active = True  # Activar la pestaña anterior
            print("Movido a: " + self.current_tab.title)
        else:
            print("No hay pestaña anterior.")

    def close_current_tab(self):
        if not self.current_tab:
            print("No hay pestañas para cerrar.")
            return

        print("Cerrando la pestaña: " + self.current_tab.title)
        
        if self.current_tab.prev:
            self.current_tab.prev.next = self.current_tab.next
        if self.current_tab.next:
            self.current_tab.next.prev = self.current_tab.prev
            self.current_tab = self.current_tab.next
        else:
            self.current_tab = self.current_tab.prev
        
        if self.current_tab:
            self.current_tab.is_active = True

# Ejemplo de uso
browser = BrowserTabs()

# Abrir nuevas pestañas con atributos adicionales
browser.open_tab("google.com", "Google", load_time=2.5)
browser.open_tab("github.com", "GitHub", load_time=3.1)
browser.open_tab("openai.com", "OpenAI", load_time=4.0)

browser.show_tabs()  # Mostrar todas las pestañas con información detallada

# Navegar entre pestañas
browser.move_to_next_tab()  # Moverse a la siguiente pestaña
browser.move_to_previous_tab()  # Moverse a la pestaña anterior

# Cerrar la pestaña actual
browser.close_current_tab()

# Mostrar las pestañas restantes
browser.show_tabs()
