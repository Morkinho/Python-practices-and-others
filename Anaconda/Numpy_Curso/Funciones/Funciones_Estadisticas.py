### Imports
import numpy as np

### Resume
'''
Buscamos el valor alto como el mínimo

'''

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m) 
print('')

print(np.amax(m)) #----> Busqueda de valor mayor de una matriz
print(np.amin(m)) #----> Busqueda de valor minimo

print(np.amin(m, 1)) #----> Busqueda de valores minimos en fila 
print(np.amin(m, 0)) #----> Busqueda de valores minimos en columna

### Para la obtención del rango de unos datos se necesita restar estos valores
#Se puede hace de la siguiente manera:

print('Obtención de rango: ')
print(np.ptp(m))
print(np.ptp(m, axis=1)) #----> Busqueda de rango en fila.
print(np.ptp(m, axis=0)) #----> Busqueda de rango en columna.

### Valores perceptiles
#Se puede hace de la siguiente manera (Solamente se puede hacer cuando los datos de la matriz son impares):


print('Obtencion de perceptil: ')
print(np.percentile(m, 50))
print(np.percentile(m, 50, axis=1)) #----> Busqueda de perceptil en fila.
print(np.percentile(m, 50, axis=0)) #----> Busqueda de perceptil en columna.

print('Obtención de mediana: ')
print(np.median(m)) #----> Obtencion de mediana
print(np.median(m, axis=0)) #----> Obtencion de mediana con columnas
print(np.median(m, axis=1)) #----> Obtencion de mediana en filas

print('Obtencion de media aritmetica: ')
print(np.mean(m)) 

### Nueva matriz, para busqueda de promedio

m2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

# Promedio ponderado:
print('')
print('Obtención de promedio: ')
print(np.average(m2))

#Desviacion estandar:
print('')
print(np.std(m2)) #----> Obtencion de desviacion