from Servicio.Catalogo_Pe import *
import os

def Menu():
    print('Menú de Catalogo de Películas'.center(50,'-'))
    print('1 - Agregá una Película')
    print('2 - Listar Películas')
    print('3 - Eliminar Películas')
    print('4 - Salir')

Menu()
x = int(input('Coloca un número: '))
while x<0 or x>4:
    print('Saliendo de la app.')
    break
if x == 1:
        y = input('Nombra la película: ')
        y = Catalogo(y)
        print('Se ha añadido la película: ')
        print(y)
        print('Con exito')


if x == 2:
            print('Estas son las películas disponibles'.center(50, '-'))
            pelicula = open('Catalogo.txt', 'r', encoding='utf8')
            print(pelicula.read())
            pelicula.close()



if x==3:
        print('Se eliminará el catálogo')
        os.remove('Catalogo.txt')
        print('El catálogo se eliminó con éxito.')
    
if x==4:
        print('El programa se cerrará')
        print('Adiós!')