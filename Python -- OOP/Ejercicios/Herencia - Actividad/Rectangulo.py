from Cl import color
from FG import figurageo

class rectangulo (figurageo, color):
    def __init__(self, ancho, alto, color) -> None:
        figurageo.__init__(self, ancho, alto)
        color.__init__(self, color)

    def CalcularArea (self):
        return self.alto * self.ancho

