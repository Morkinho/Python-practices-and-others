import numpy as np

cuerpo = np.array([[2, 7, 3],[2, 8, 2], [1, 3, 1]])
r = np.array([[1],[1],[0]])

print(np.linalg.solve(cuerpo, r))