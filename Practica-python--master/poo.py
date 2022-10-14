class Camiseta:
    def __init__(self, marca, precio, talla, color):
        self.marca = marca 
        self.precio = precio
        self.talla = talla
        self.color = color
        self.rebajada = False

    def aplicarDescuento(self, porcentaje):
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebajada = True

    def infoProducto(self):
        info = f"Descripcion de la camiseta:\nMarca: {self.marca}\nPrecio: {self.precio:.2f}\nTalla: {self.talla}\nColor: {self.color}\n"
        if self.rebajada:
            info += "Este producto esta rebajado"
        return info

camiseta = Camiseta("Nike", 19.99, "S", "lila")
camisetaAdidas = Camiseta("Adidas", 30, "M", "Rojo")

camisetaAdidas.aplicarDescuento(50)
camiseta.aplicarDescuento(20)
print(camiseta.infoProducto())
print("#########")
print(camisetaAdidas.infoProducto())