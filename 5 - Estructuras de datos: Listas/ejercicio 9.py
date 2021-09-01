# Ejercicio 9
# Realiza un programa que calcule la matriz transpuesta.

m = [[1, 2, 3], [4, 5, 6]]

t = []

for i in range(len(m[0])):
    t.append([])
    for j in range(len(m)):
        t[i].append(m[j][i])
    if len(t) == len(m[0]):
        print(t, end=" ")