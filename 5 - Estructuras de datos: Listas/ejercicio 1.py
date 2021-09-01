# Ejercicio 1
# Crea un programa que lea una secuencia de caracteres, guarde cada caracter en una posición de una lista y
# finalmente muestre la secuencia invertida.

n = int(input("Agregue la cantidad de una secuencia: "))
lista = []

for x in range(n):
    lista.append(input("agregue un caracter: "))

print(list(reversed(lista)))

