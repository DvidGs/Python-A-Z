# Ejercicio 10
# Dada una matriz, crea un diccionario que guarde el número de filas, el de columnas y cada fila en una entrada
# de un diccionario.

M = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 2, 3, 4]]
d = {"filas": len(M), "columnas": len(M[0])}

for i in range(len(M)):
    d["fila " + str(i)] = M[i]

print(d)
