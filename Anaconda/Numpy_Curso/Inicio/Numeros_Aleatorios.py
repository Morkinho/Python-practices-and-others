import numpy as np

#Numeros Aleatorios son numeros que no se pueden predecir logicamente.

print('Inicio de valor randomizado con enteros'.center(50,'-'))
m = np.random.randint(10, size=(3,3))
print(m)

print('Inicio de valor randomizado con floats'.center(50,'-'))
mf = np.random.rand(2,2) #Se usa directamente la fila y columna de la matriz.
print(mf)

print('Devolviendo un solo valor'.center(50,'-'))
me = np.random.choice([3,9,5,4,2,1], size=(2,3)) #Choise extrae un valor random dentro de esa matriz
print(me)
