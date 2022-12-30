from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color) -> None:
        #super().__init__()
        FiguraGeometrica.__init__(self, lado, lado)  #De esta forma podemos mandar a llamar a la clase de FiguraGeometrica
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
        