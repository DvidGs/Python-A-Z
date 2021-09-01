# Ejercicio 2
# Crea un programa que lea dos strings de la misma longitud, los guarde intercalados en una lista. Por último,
# mostrar el contenido de la lista.
# Por ejemplo, si introducimos hola caracola y adios marieta, debería mostrarse haodleao sc
# amraarcioeltaa.

frase1 = str(input("texto 1: "))
frase2 = str(input("texto 2: "))
lista = []
for l in range(len(frase1)):
    lista.append(frase1[l])
    lista.append(frase2[l])
print(lista)
