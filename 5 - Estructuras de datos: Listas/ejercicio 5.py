# Ejercicio 5
# Crea un programa que lea una matriz 3 x 3 y devuelva el máximo de cada fila.

matrix = [[1, 2, 3], [4, 5, 6], [9, 7, 8]]
c = 0
a = 0
for row in matrix:          # Accedemos a las filas de la matrix
  for element in row:       # Accedemos a los elementos de las filas
    #print(element)
    c += 1
    if element >= a:
      a = element
    if c == 3:
      print(a)
      c = 0
      a = 0




