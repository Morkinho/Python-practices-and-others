import numpy as np

print('Matriz 2D: ')
m2d = np.array([[1,2,3],[4,5,6]]) #Primer Corchete ---> Primera Fila // Segundo Corchete ---> Segunda Fila
print(m2d)

print('Pasar una lista a una Matriz'.center(50, '-'))
l1 = [1,2,3,4,5]
matriz = np.array(l1) # Se agrega el valor de la lista 'L1' a el array
print(matriz)


print('Poner una lista doble en una matriz 2x2'.center(50, '-'))
l2 = [[1,2,3],[4,5,6]]
matriz2 = np.array(l2)
print(matriz2)


print('Poner una lista triple en una matriz 3x3'.center(50, '-'))
l3 = [[1,2,3],[4,5,6],[7,8,9]]
matriz3 = np.array(l3)
print(matriz3)

### Forma Simplificada:
print('Forma simple')
m = np.arange(15).reshape(3,5)
print(m)

# arange le otorga una cantidad de elementos a usar a la matriz.
# reshape('Le indicamos las filas, le seguimos con las columnas')