#with open('prueba.txt', 'r', encoding='utf8') as archivo:
#    print(archivo.read())

from Manejo_Archivos_ import *

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())