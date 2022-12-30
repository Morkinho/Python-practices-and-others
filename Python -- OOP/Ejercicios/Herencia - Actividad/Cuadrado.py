from Cl import color
from FG import figurageo

class cuadrado (figurageo, color):
    def __init__(self, lado, color) -> None:
        figurageo.__init__(self, lado, lado)
        color.__init__(self, color)

    def CalcularArea (self):
        return self.alto * self.ancho
    

        