import array as ar
import numpy as np

#Generación simple, bajo array:

matriz = ar.array('i', [1,2,3,4,5])

for ar in matriz:
    print(ar)

print('Fin de Array, comienzo de Numpy'.center(50, '-'))

#

matriz2 = np.array([1,2,3,4,5])
print(matriz2)

######

#Con los Arrays se puede hacer operaciones Aritméticas:

print('Inicio de operaciones de matrices: ')
a = np.array([1,2,3])
b = np.array([4,5,6])



def op_arit():
    return f'''
    Los valores dados son:
    {a} y {b}

    Suma:
    {a+b}

    Resta:
    {a-b}

    Multiplicacion:
    {a*b}

    Division:
    {a/b}
    
    Fin de operaciones.

'''
print(op_arit())