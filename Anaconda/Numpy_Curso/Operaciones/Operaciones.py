import numpy as np

#Ubicar elementos por posición:

m = np.arange(24).reshape(4,6)
print(m)
print(m[3,4])

print('Inicio de Ordenamiento de números'.center(50, '-'))
#ordenar los elementos de manera ascendente
m1 = np.array([7,9,4,5,124,5,1])
print(np.sort(m1))


print('Inicio potencia de matrices'.center(50, '-'))
#Elevar los valores de la matriz
m2 = np.array([2,3])
print(np.power(m2, 3))


print('Inicio de clasificación de matrices'.center(50, '-'))
#Clasificar los números:
m3 = np.array([2,3,4,5,6,7,8,9,10,11])
print(np.array(m3>=4))

print('Inicio de busqueda de un número máximo en la matriz'.center(50, '-'))
print(np.array(m1.max()))

print('Inicio de busqueda de un número minimo en la matriz'.center(50, '-'))
print (np.array(m1.min()))


print('Inicio de Combinación de matrices'.center(50, '-'))
print(np.concatenate((m1, m2)))