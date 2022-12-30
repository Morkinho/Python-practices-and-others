class cubo:
    def __init__(self, ancho, alto, profundo) -> None:
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def volumen (self):
        return self.ancho * self.alto * self.profundo

PrimerValor = int(input(' Coloca la anchura del cubo: '))
SegundoValor = int(input(' Coloca el alto del cubo: '))
TercerValor = int(input(' Coloca la profundidad del cubo: '))

calculo = cubo(PrimerValor, SegundoValor, TercerValor)

print(f'El volumen el cubo es {calculo.volumen()}')