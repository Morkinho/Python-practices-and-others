import numpy as np

m = np.arange(20).reshape(4,5)
print(m.shape) #Shape mide las filas y las columnas de la matriz
print(m.ndim) #ndim mide las dimenciones
print(m.size) #Mide los elementos
print(m)

####

#Generar matrices de 0
print('Inicio de Matriz de 0'.center(50, '-'))
n = np.zeros((3,4))
print(n)

#Generar matrices con un número inicial, con un número final y un limitador (x,x,x)
print('Inicio de Matriz limitada'.center(50, '-'))
h = np.linspace(99,1,3)
print(h)

#Matriz de 3 dimensiones:
print('Inicio de Matriz con 3Dimensiones'.center(50, '-'))
D = np.arange(27).reshape(3,3,3)
print(D)