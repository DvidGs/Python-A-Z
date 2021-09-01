# Ejercicio 7
# Crea una matriz de n × m y asigna los valores manualmente. El programa debe indicar si la suma de cada
# columna es el mismo valor.

A = [[1, 2, 3], [3, 2, 1], [-1, -2, -3]]
B = [[3, 2, 1], [-3, -1, -1], [1, 2, 3]]

m = len(A)
n = len(A[0])

if len(A) == len(B) and len(A[0]) == len(B[0]):

    C = []
    for i in range(n):
        C.append([])
        for j in range(m):
            C[i].append(A[i][j] + B[i][j])

    print("\n=== Matriz A + B ===")
    for i in range(n):
        for j in range(m):
            print(C[i][j], end="  " if C[i][j] >= 0 else " ")
        print("")