import numpy as np
"""
m = np.array([[1,-1,2],[3,2,0]])
print(m)

### Hacer una matriz de una sola columna:
print('Matriz de una columna')
m1 = np.array([[1],[2],[3]])
print(m1)

print('Matriz traspuesta')
print(np.transpose(m))

"""

# Ax = b

a = np.array([[2,1,-2],[3,0,1],[1,1,-1]])
b = np.array([[-3],[5],[-2]])

print(np.linalg.solve(a, b))