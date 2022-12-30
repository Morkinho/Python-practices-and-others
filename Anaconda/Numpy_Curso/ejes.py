import numpy as np

print('Coordenadas')

m = np.array([[0,1,2],[4,2,3]])
m2 = np.array([[1,1,1,],[1,1,1]])
print(m)
print('')

print(np.sum(m, axis=0)) #Se hace las sumas de las columnas de arriba hacia abajo.
print(np.sum(m, axis=1)) #Hace la suma de las filas de izq. a der.

print('')
print('Concatenar hacia abajo')
print(np.concatenate([m, m2], axis=0)) #Unifica las matrices haciendola mas larga.

print('')
print('Concatenar a la derecha')
print(np.concatenate([m,m2], axis=1))