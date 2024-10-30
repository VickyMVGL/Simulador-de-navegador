class Pagina:
    def __init__(self, html, ip, dominio):
        self.html = html
        self.ip = ip
        self.dominio = dominio

    def vizualizar(self):
        print("Estas visitando la pagina: ", self.dominio)
        print("---------------------------------------------")
        print("Nombre de dominio: ", self.dominio)
        print("Direccion IP: " , self.ip)
        print("Direccion del archivo html: ", self.html)
        print("")
