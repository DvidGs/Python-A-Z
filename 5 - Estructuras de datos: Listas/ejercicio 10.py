# Ejercicio 10
# Crea un programa que pida al usuario la dimensión y cree la matriz identidad de orden correspondiente con
# numpy.

import numpy as np

D = int(input("Agregar dimensión: "))

matriz = np.identity(D)

print(matriz)
