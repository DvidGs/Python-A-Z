# Ejercicio 8
# Crear un programa determina si la matriz introducida manualmente (tanto sus dimensiones como los ele-
# mentos) se trata de la matriz identidad. Recuerda que la matriz identidad debe ser una matriz cuadrada.

A = [[1, 2, 3], [3, 2, 1], [-1, -2, -3]]
B = [[3, 2, 1], [-3, -1, -1], [1, 2, 3]]

m = len(A)
n = len(A[0])

if m == n:
    print("Es una matriz cuadrada")
else:
    print("No es una matriz cuadrada")
