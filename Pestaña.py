class Tab:
    def __init__(self, url, title, load_time=0):
        self.url = url
        self.title = title
        self.load_time = load_time  
        self.is_active = False  
        self.history = [url]  
        self.next = None  
        self.prev = None  

    def visit_url(self, new_url):
        
        self.history.append(new_url)
        self.url = new_url

    def show_info(self):
        
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
            self.current_tab.is_active = True  
        else:
            temp = self.current_tab
            while temp.next:  
                temp = temp.next
            temp.next = new_tab
            new_tab.prev = temp

    def open_a_tab(self, numero):
        if numero > len(self.history):
            print("No existe esa pestaña")
        else:
            temp = self.current_tab
            cont = 0
            while cont < numero:  
                temp = temp.next
                cont += 1
            temp.show_info()

    def show_tabs(self):
        temp = self.current_tab
        while temp:
            temp.show_info()  
            temp = temp.next

    def move_to_next_tab(self):
        if self.current_tab and self.current_tab.next:
            self.current_tab.is_active = False  
            self.current_tab = self.current_tab.next
            self.current_tab.is_active = True  
            print("Movido a: " + self.current_tab.title)
        else:
            print("No hay más pestañas.")

    def move_to_previous_tab(self):
        if self.current_tab and self.current_tab.prev:
            self.current_tab.is_active = False  
            self.current_tab = self.current_tab.prev
            self.current_tab.is_active = True  
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
"""
# Abrir nuevas pestañas con atributos adicionales
browser.open_tab("google.com", "Google", load_time=2.5)
browser.open_tab("github.com", "GitHub", load_time=3.1)
browser.open_tab("openai.com", "OpenAI", load_time=4.0)
print("---------------1-----------------")
browser.show_tabs()  # Mostrar todas las pestañas con información detallada

# Navegar entre pestañas
browser.move_to_next_tab()  # Moverse a la siguiente pestaña
browser.move_to_previous_tab()  # Moverse a la pestaña anterior
print("---------------2-----------------")

# Cerrar la pestaña actual
browser.close_current_tab()
print("--------------3------------------")

# Mostrar las pestañas restantes
browser.show_tabs()
"""
