from Cuadrado import cuadrado
from Rectangulo import rectangulo

print('Creacion Objeto Cuadrado'.center (50, '-'))
cuadrado1 = cuadrado (5, 'Rojo')
print (f'Calculo area Rectangulo: {cuadrado1.CalcularArea()}')


print('Creacion Objeto Rectangulo'.center (50, '-'))
rectangulo1 = rectangulo (15, 54, color='Blanco')
print (f'Calculo area Rectangulo: {rectangulo1.CalcularArea()}')
print(rectangulo1)